import keras
from keras.layers import Conv1D, GlobalMaxPooling1D, Input, Dense, concatenate, Activation, Dropout
from keras.models import Model
from keras.layers.embeddings import Embedding
import numpy as np
from typing import Iterable, Any
#import numpy as np 
#import tensorflow as tf 
from .classifier_input import ClassifierInput
from .model_dao import ModelDao
from .metrics import Metrics
from .metrics_keras_callback import MetricsKerasCallback
from .classifier_lab import ClassifierLab, LabReport
#from keras.wrappers.scikit_learn import k
#np.random.seed(5)
#tf.set_random_seed(5)


class CnnLab(ClassifierLab):

    def __init__(self, input:ClassifierInput, dao: ModelDao):
        super().__init__(input, dao)

    def train_by_stratifiedkfold(self, folds=10) -> LabReport:
        input = self._input
        labreport = LabReport.create()
        for x_train, x_val, y_train, y_val in input.train_val_stratifiedkfold(input.x, input.y, folds=folds):
            model = self.create_model(input)   
            modelname = self.get_an_id()
            metrics_callback = MetricsKerasCallback.create(modelname, x_train, y_train, x_val, y_val, input.categories, labreport)
            model.fit(x_train, 
                    y_train, 
                    batch_size=32,
                    epochs=5,
                    validation_data=(x_val, y_val), 
                    callbacks=[metrics_callback], 
                    shuffle=False,
                    verbose=False)
            self._dao.save_keras_weights(modelname, model)
        return labreport

    def create_model(self, input:ClassifierInput):
        
            input_comments = Input(shape=(input.comment_max_length,), dtype='int32')
            comment_encoder = Embedding(input_dim=input.vocab_size, output_dim=300, input_length=input.comment_max_length, weights=[input.embedding_matrix], trainable=False)(input_comments)
            bigram_branch = Conv1D(filters=100, kernel_size=2, padding='valid', activation='relu', strides=1)(comment_encoder)
            bigram_branch = GlobalMaxPooling1D()(bigram_branch)
            trigram_branch = Conv1D(filters=100, kernel_size=3, padding='valid', activation='relu', strides=1)(comment_encoder)
            trigram_branch = GlobalMaxPooling1D()(trigram_branch)
            fourgram_branch = Conv1D(filters=100, kernel_size=4, padding='valid', activation='relu', strides=1)(comment_encoder)
            fourgram_branch = GlobalMaxPooling1D()(fourgram_branch)
            merged = concatenate([bigram_branch, trigram_branch, fourgram_branch], axis=1)
            merged = Dense(256, activation='relu')(merged)
            merged = Dropout(0.5)(merged)
            merged = Dense(4)(merged)
            output = Activation('softmax')(merged)
            model = Model(inputs=[input_comments], outputs=[output])
            model.compile(loss='sparse_categorical_crossentropy', 
                        optimizer='adam', 
                        metrics=[keras.metrics.sparse_categorical_accuracy]
            )
            return model

    def test(self, modelname:str, input:ClassifierInput) -> Metrics:
        model = self.create_model(input)
        model = self._dao.get_keras_weights(modelname, model)
        y_pred = model.predict(input.x)
        y_pred_sparsed = np.argmax(y_pred, axis=1)
        metrics = Metrics.create(input.y, y_pred_sparsed, y_pred, input.categories)
        return metrics

    def predict(self, modelname, input:ClassifierInput) -> Iterable[Any]:
        model = self.create_model(input)
        model = self._dao.get_keras_weights(modelname, model)
        y_pred = model.predict(input.x)
        y_pred_sparsed = np.argmax(y_pred, axis=1)
        labeled_predictions = np.array([input.categories[index] for index in y_pred_sparsed], dtype=object)
        return labeled_predictions
     