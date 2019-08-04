from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from keras.callbacks import Callback
from keras.models import Model
import numpy as np
from .classifier_lab import LabReport, ModelReport
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
        self ._epochs = []

    def on_epoch_end(self, epoch, logs):
        model_report = self._create_model_report()
        self._epochs.append(model_report)
 
    def on_train_end(self, logs={}):
        model_report = self._create_model_report()
        model_report.epochs = self._epochs
        self._lab_report.add(model_report)

    def _create_model_report(self) -> ModelReport:
        model_report = ModelReport.create(self._modelname, 
            self._categories,
            lambda x: self._predict(x, self.model),
            self._x_train, self._x_val, self._y_train, self._y_val)
        return model_report

    def _predict(self, x, model:Model):
        y_pred = model.predict(x)
        y_pred_sparsed = np.argmax(y_pred, axis=1)
        return y_pred_sparsed, y_pred

    @classmethod
    def create(cls, modelname, x_train, y_train, x_val, y_val, categories, lab_report:LabReport):
        return cls(modelname, x_train, y_train, x_val, y_val, categories, lab_report)