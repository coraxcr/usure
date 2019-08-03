from keras.layers import Conv1D, GlobalMaxPooling1D, Input, Dense, concatenate, Activation, Dropout
from keras.models import Model
from keras.layers.embeddings import Embedding
from keras.callbacks import ModelCheckpoint
import keras
import numpy as np 
import tensorflow as tf 
from .classifier_input import ClassifierInput
from .metrics_keras_callback import MetricsKerasCallback
import usure.common.logging as usurelogging
from usure.config import config 
from .classifier_lab import ClassifierLab
from .model_dao import ModelDao
#np.random.seed(5)
#tf.set_random_seed(5)


class CnnLab(ClassifierLab):

    def __init__(self, input:ClassifierInput, dao: ModelDao):
        super().__init__(input, dao)
        
    @property
    def name(self):
        return f"cnn.{self._id}-{self._input.embeddings_name}.h5"

    def research(self):

        input = self._input
        
        input_comments = Input(shape=(input.comment_max_length,), dtype='int32')
        comment_encoder = Embedding(input.vocab_size, 300, weights=[input.embedding_matrix], input_length=input.comment_max_length, trainable=False)(input_comments)
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
        
        #model.summary(print_fn=usurelogging.info)


        x_train, x_val, y_train, y_val = input.train_val_split(input.x, input.y)
        metrics = MetricsKerasCallback.create(x_train, y_train, x_val, y_val, input.categories) 

        model.fit(x_train, 
                  y_train, 
                  batch_size=32,
                  epochs=5,
                  validation_data=(x_val, y_val), 
                  callbacks=[metrics], 
                  shuffle=False)  
        
        self._train_report = metrics.train_reporter
        self._validation_report = metrics.val_reporter

        self._dao.save_keras(self.name, model)