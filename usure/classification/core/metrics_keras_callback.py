from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from keras.callbacks import Callback
from keras.models import Model
import numpy as np
from .classifier_lab import LabReport
from .metrics import Metrics

class MetricsKerasCallback(Callback):

    def __init__(self, modelname, x_train, y_train, x_val, y_val, categories, lab_report:LabReport):
        self._modelname = modelname
        self._x_train = x_train
        self._y_train = y_train
        self._x_val = x_val
        self._y_val = y_val
        self._categories = categories
        self._lab_report = lab_report
    
    def on_train_end(self, logs={}):
        train_prediction = self._predict(self._x_train, self.model)
        val_prediction = self._predict(self._x_val, self.model)
        training_metrics = Metrics.create(self._y_train, train_prediction[0], train_prediction[1], self._categories)
        validation_metrics = Metrics.create(self._y_val, val_prediction[0], val_prediction[1], self._categories)
        self._lab_report.add(self._modelname,training_metrics, validation_metrics)

    def _predict(self, x, model:Model):
        y_pred = model.predict(x)
        y_pred_sparsed = np.argmax(y_pred, axis=1)
        return y_pred_sparsed, y_pred

    @classmethod
    def create(cls, modelname, x_train, y_train, x_val, y_val, categories, lab_report:LabReport):
        return cls(modelname, x_train, y_train, x_val, y_val, categories, lab_report)