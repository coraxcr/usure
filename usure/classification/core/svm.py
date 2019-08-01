from typing import Iterable
import os

import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, LabelBinarizer
from sklearn import metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm


#reproductability
from numpy.random import seed
seed(10)

from .labeled_comments import LabeledComments
from .wordvectors import WordVectors
import usure.common.logging as usurelogging
from usure.config import config 


class Svn:

    def __init__(self, labeledcom:LabeledComments, wv:WordVectors):
        self._labeledcom = labeledcom
        self._wv = wv
    
    def convert_to_padded_sequences(self, tokenizer:Tokenizer, sentences:Iterable[str]):
        sequences = tokenizer.texts_to_sequences(sentences)
        padded_sequences = pad_sequences(sequences, maxlen=20)
        return padded_sequences

    def map_to_embedding_matrix(self, tokenizer:Tokenizer, wv:WordVectors):
        embedding_matrix = np.zeros((len(tokenizer.index_word)+1, 300))
        for word, i in tokenizer.word_index.items():
            if word in wv.wordvectors:
                embedding_matrix[i] = wv.wordvectors[word]
        return embedding_matrix

    
    def map_to_one_hot_labels(self, labels:Iterable[str]):#inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
        lb = LabelBinarizer()
        lb.fit(labels)
        one_hot =  lb.transform(labels)
        return one_hot, lb.classes_
    
    def map_to_integers(self, labels:Iterable[str]):
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(labels)
        #integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        return integer_encoded, label_encoder.classes_


    def work(self):
        usurelogging.info(type(self).__name__)
        max_words = 20#len(max(self._labeledcom.comments, key=lambda comment: len(comment.split())).split()) + 5
        
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(self._labeledcom.comments)
        embedding_matrix = self.map_to_embedding_matrix(tokenizer, self._wv)
        x = self.convert_to_padded_sequences(tokenizer, self._labeledcom.comments)
        x = [np.mean(np.array([ embedding_matrix[word_index] for word_index in comment]), axis=0) for comment in x]
        y, classes = self.map_to_integers(self._labeledcom.labels)

        x, x_dev, y, y_dev = train_test_split(x, y, test_size=0.1, random_state=42)

        clf = svm.LinearSVC()
        clf.fit(x, y)

        y_pred = clf.predict(x_dev)
        y_pred_train = clf.predict(x)
        #y_dev = np.argmax(y_dev, axis=1)
        #y_pred = np.argmax(y_pred, axis=1)

        usurelogging.info(os.linesep+metrics.classification_report(y_dev, y_pred, target_names=classes))
        #usurelogging.info(metrics.confusion_matrix(y_dev, y_pred))
        usurelogging.info(f"Better categorical accuracy for TRAIN {self._labeledcom.name} {self._wv.name} is {metrics.accuracy_score(y, y_pred_train)}.")
        usurelogging.info(f"Better categorical accuracy for DEV {self._labeledcom.name} {self._wv.name} is {metrics.accuracy_score(y_dev, y_pred)}.")
