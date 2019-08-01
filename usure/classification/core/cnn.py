from typing import Iterable
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras import utils
from keras.layers import Conv1D, GlobalMaxPooling1D, Input, Dense, concatenate, Activation, Dropout, Flatten
from keras.models import Model, Sequential
from keras.layers.embeddings import Embedding
from keras.callbacks import ModelCheckpoint
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, LabelBinarizer
from sklearn import metrics
import pandas as pd
from sklearn.model_selection import train_test_split
import keras
import numpy.random 
numpy.random.seed(10)
import tensorflow as tf 
tf.set_random_seed(11)

from .labeled_comments import LabeledComments
from .wordvectors import WordVectors
from .metrics_keras_callback import MetricsKerasCallback
import usure.common.logging as usurelogging
from usure.config import config 

import sklearn 

class Cnn:

    def __init__(self, labeledcom:LabeledComments, wv:WordVectors):
        self._labeled_comments = labeledcom
        self._wv = wv
    
    def convert_to_padded_sequences(self, tokenizer:Tokenizer, sentences:Iterable[str], sequence_max_length:int):
        sequences = tokenizer.texts_to_sequences(sentences)
        padded_sequences = pad_sequences(sequences, maxlen=20)
        return padded_sequences

    def create_embedding_matrix(self, tokenizer:Tokenizer, wv:WordVectors):
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
        comment_max_length = 20#len(max(self._labeledcom.comments, key=lambda comment: len(comment.split())).split()) + 5
        
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(self._labeled_comments.comments)

        embedding_matrix = self.create_embedding_matrix(tokenizer, self._wv)

        x = self.convert_to_padded_sequences(tokenizer, self._labeled_comments.comments, comment_max_length)

        y, classes = self.map_to_integers(self._labeled_comments.labels)

        x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.1, random_state=42)

        vocab_size = len(tokenizer.index_word)+1

        input_comments = Input(shape=(comment_max_length,), dtype='int32')
        comment_encoder = Embedding(vocab_size, 300, weights=[embedding_matrix], input_length=comment_max_length, trainable=False)(input_comments)
        bigram_branch = Conv1D(filters=100, kernel_size=2, padding='valid', activation='relu', strides=1)(comment_encoder)
        bigram_branch = GlobalMaxPooling1D()(bigram_branch)
        trigram_branch = Conv1D(filters=100, kernel_size=3, padding='valid', activation='relu', strides=1)(comment_encoder)
        trigram_branch = GlobalMaxPooling1D()(trigram_branch)
        fourgram_branch = Conv1D(filters=100, kernel_size=4, padding='valid', activation='relu', strides=1)(comment_encoder)
        fourgram_branch = GlobalMaxPooling1D()(fourgram_branch)
        merged = concatenate([bigram_branch, trigram_branch, fourgram_branch], axis=1)

        merged = Dense(256, activation='relu')(merged)
        merged = Dropout(0.2)(merged)
        merged = Dense(4)(merged)
        output = Activation('softmax')(merged)
        model = Model(inputs=[input_comments], outputs=[output])

        model.compile(loss='sparse_categorical_crossentropy', 
                      optimizer='adam', 
                      metrics=[keras.metrics.sparse_categorical_accuracy]
        )

        model.summary(print_fn=usurelogging.info)

        filepath = config.classification+"/"+"cnn.h5"
        checkpoint = ModelCheckpoint(filepath, 
            monitor='val_sparse_categorical_accuracy', 
            verbose=0, 
            save_weights_only = False,
            save_best_only=True, 
            mode='max')

        metrics = MetricsKerasCallback.create(x_train, y_train, x_val, y_val) 

        history = model.fit(x_train, y_train, batch_size=32, epochs=2,
         validation_data=(x_val, y_val), callbacks=[checkpoint, metrics], shuffle=False)  
        
        #df = pd.DataFrame(history.history)
        #usurelogging.infonl(df.to_string(float_format=lambda n: format(n, '#.2g')))


        usurelogging.infonl(metrics.val_reporter.to_string())
        usurelogging.infonl(metrics.train_reporter.to_string())
        

        #model = keras.models.load_model(filepath)

        y_val_pred = model.predict(x_val)
        print(sklearn.metrics.accuracy_score(y_val, np.argmax(y_val_pred, axis=1)))

        #keras.losses.categorical_crossentropy()

        #import pickle
        #tokenizer_path = config.classification+"/"+"tokenizer.pickler"
        #with open(tokenizer_path, 'wb') as file:
        #    pickle.dump(tokenizer, file, protocol=pickle.HIGHEST_PROTOCOL)
        #use delete here
        #with open(tokenizer_path, 'rb') as file:
        #    tokenizer = pickle.load(file)
        #https://stackoverflow.com/questions/48041867/why-is-accuracy-different-between-keras-model-fit-and-model-evaluate
        