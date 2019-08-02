from typing import Iterable
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.preprocessing import LabelEncoder, LabelBinarizer
from sklearn.model_selection import train_test_split
from .wordvectors import WordVectors
from .labeled_comments import LabeledComments

np.random.seed(5)
import tensorflow as tf 
tf.set_random_seed(5)

class ClassifierInput:

    def __init__(self, labeled_comments:LabeledComments, wv:WordVectors):
        self._labeled_comments = labeled_comments
        self._wv = wv
        self._tokenizer = Tokenizer()
        self._tokenizer.fit_on_texts(self._labeled_comments.comments)
        self._set_properties()

    @property
    def vocab_size(self):
        return self._vocab_size

    @property
    def comment_max_length(self):
        return self._comment_max_length

    @property 
    def embedding_matrix(self):
        return self._embedding_matrix

    @property
    def embeddings_name(self):
        return self._wv.name

    @property 
    def x(self):
        return self._x
    
    def x_mean(self):
        return [np.mean(np.array([self.embedding_matrix[word_index] for word_index in comment]), axis=0) for comment in self.x]
    
    @property 
    def y(self):
        return self._y
    
    @property 
    def categories(self):
        return self._categories

    def train_val_split(self, x, y, val_size=0.1):
        return train_test_split(x, y, test_size=val_size, random_state=42, shuffle=False)

    def _set_properties(self):
        self._comment_max_length = len(max(self._labeled_comments.comments, key=lambda comment: len(comment.split())).split()) + 5
        self._vocab_size = len(self._tokenizer.index_word)+1
        self._embedding_matrix = self._create_embedding_matrix(self._tokenizer, self._wv)
        self._x = self._convert_to_padded_sequences(self._tokenizer, self._labeled_comments.comments, self._comment_max_length)
        self._y, self._categories = self._map_to_integers(self._labeled_comments.labels)
        
    def _map_to_integers(self, labels:Iterable[str]):
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(labels)
        return integer_encoded, label_encoder.classes_

    def _create_embedding_matrix(self, tokenizer:Tokenizer, wv:WordVectors):
        embedding_matrix = np.zeros((len(tokenizer.index_word)+1, 300))
        for word, i in tokenizer.word_index.items():
            if word in wv.wordvectors:
                embedding_matrix[i] = wv.wordvectors[word]
        return embedding_matrix

    def _convert_to_padded_sequences(self, tokenizer:Tokenizer, sentences:Iterable[str], sequence_max_length:int):
        sequences = tokenizer.texts_to_sequences(sentences)
        padded_sequences = sequence.pad_sequences(sequences, maxlen=sequence_max_length)
        return padded_sequences

    def _map_to_one_hot_labels(self, labels:Iterable[str]):
        lb = LabelBinarizer()
        lb.fit(labels)
        one_hot =  lb.transform(labels)
        return one_hot, lb.classes_