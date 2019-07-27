from typing import Iterable
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras import utils
from keras.layers import Conv1D, GlobalMaxPooling1D, Input, Dense, concatenate, Activation, Dropout, Flatten
from keras.models import Model, Sequential
from keras.layers.embeddings import Embedding
from keras.callbacks import ModelCheckpoint
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

from .labeled_comments import LabeledComments
from .wordvectors import WordVectors


class CNN1D:

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
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(labels)
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
        return onehot_encoded
    

    def work(self):

        max_words = 20#len(max(self._labeledcom.comments, key=lambda comment: len(comment.split())).split()) + 5
        
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(self._labeledcom.comments)
        embedding_matrix = self.map_to_embedding_matrix(tokenizer, self._wv)
        x = self.convert_to_padded_sequences(tokenizer, self._labeledcom.comments)
        y = self.map_to_one_hot_labels(self._labeledcom.labels)


        input_comments = Input(shape=(max_words,), dtype='int32')
        tweet_encoder = Embedding(len(tokenizer.index_word)+1, 300, weights=[embedding_matrix], input_length=max_words, trainable=False)(input_comments)
        bigram_branch = Conv1D(filters=100, kernel_size=2, padding='valid', activation='relu', strides=1)(tweet_encoder)
        bigram_branch = GlobalMaxPooling1D()(bigram_branch)
        trigram_branch = Conv1D(filters=100, kernel_size=3, padding='valid', activation='relu', strides=1)(tweet_encoder)
        trigram_branch = GlobalMaxPooling1D()(trigram_branch)
        fourgram_branch = Conv1D(filters=100, kernel_size=4, padding='valid', activation='relu', strides=1)(tweet_encoder)
        fourgram_branch = GlobalMaxPooling1D()(fourgram_branch)
        merged = concatenate([bigram_branch, trigram_branch, fourgram_branch], axis=1)

        merged = Dense(256, activation='relu')(merged)
        merged = Dropout(0.2)(merged)
        merged = Dense(4)(merged)
        output = Activation('softmax')(merged)
        model = Model(inputs=[input_comments], outputs=[output])
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.summary()   

        #filepath="CNN_best_weights.{epoch:02d}-{val_acc:.4f}.hdf5"
        #checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
        #model.fit(x_train_seq, y_train, batch_size=32, epochs=5,
        #          validation_data=(x_val_seq, y_validation), callbacks = [checkpoint]) 

        model.fit(x, y, batch_size=32, epochs=5, validation_split=0.1)   