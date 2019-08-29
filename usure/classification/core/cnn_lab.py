import keras
from keras.layers import Conv1D, GlobalMaxPooling1D, Input, Dense, concatenate, Activation, Dropout
from keras.models import Model, Sequential
import numpy as np
from typing import Iterable, Any, Tuple
from .classifier_input import ClassifierInput
from .model_dao import ModelDao
from .metrics import Metrics
from .metrics_keras_callback import MetricsKerasCallback
from .classifier_lab import ClassifierLab, LabReport


class CnnLab(ClassifierLab):

    def __init__(self, dao: ModelDao):
        super().__init__(dao)

    def train_by_stratifiedkfold(self, input:ClassifierInput, folds=10) -> LabReport:
        labreport = LabReport.create()
        for x_train, x_val, y_train, y_val in self.train_val_stratifiedkfold(input.x_vectorized, input.y_indexes, folds=folds):
            model = self.create_model()   
            modelname = self.get_an_id()
            metrics_callback = MetricsKerasCallback.create(modelname, x_train, y_train, x_val, y_val, input.categories, labreport)
            model.fit(x_train, 
                    y_train, 
                    batch_size=50,
                    epochs=5,
                    validation_data=(x_val, y_val), 
                    callbacks=[metrics_callback], 
                    shuffle=False,
                    verbose=False)
            self._dao.save_keras(modelname, model)
        return labreport

    def create_model(self):
        comment_max_length = 20
        vector_size = 300
        input_comments = Input(shape=(comment_max_length, vector_size), dtype='float')
        bigram_branch = Conv1D(filters=100, kernel_size=3, padding='valid', activation='relu', strides=1)(input_comments)
        bigram_branch = GlobalMaxPooling1D()(bigram_branch)
        trigram_branch = Conv1D(filters=100, kernel_size=4, padding='valid', activation='relu', strides=1)(input_comments)
        trigram_branch = GlobalMaxPooling1D()(trigram_branch)
        fourgram_branch = Conv1D(filters=100, kernel_size=5, padding='valid', activation='relu', strides=1)(input_comments)
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

    def test(self, model_name:str, test_input:ClassifierInput) -> Tuple[Metrics, Iterable[str]]:
        model = self._dao.get_keras(model_name)
        #model.summary()
        y_pred = model.predict(test_input.x_vectorized)
        y_pred_sparsed = np.argmax(y_pred, axis=1)
        metrics = Metrics.create(test_input.y_indexes, y_pred_sparsed, y_pred, test_input.categories)
        labeled_predictions = np.array([test_input.categories[index] for index in y_pred_sparsed], dtype=object)
        return metrics, labeled_predictions

    def predict(self, model_name, input:ClassifierInput) -> Iterable[str]:
        model = self._dao.get_keras(model_name)
        y_pred = model.predict(input.x_vectorized)
        y_pred_sparsed = np.argmax(y_pred, axis=1)
        labeled_predictions = np.array([input.categories[index] for index in y_pred_sparsed], dtype=object)
        return labeled_predictions
     