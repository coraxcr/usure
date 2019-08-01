from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from keras.callbacks import Callback
from keras.models import Model
import numpy as np
from .metrics_reporter import MetricsReporter

class MetricsKerasCallback(Callback):

    def __init__(self, x_train, y_train, x_val, y_val):
        self._x_train = x_train
        self._x_val = x_val
        self._train_reporter = MetricsReporter.create(y_train)
        self._val_reporter = MetricsReporter.create(y_val)
    
    def on_epoch_end(self, epoch, logs={}):
        self._train_reporter.add_calculation(self._predict(self._x_train, self.model))
        self._val_reporter.add_calculation(self._predict(self._x_val, self.model))

    def _predict(self, x, model:Model):
        y_pred = model.predict(x)
        y_pred_sparsed = np.argmax(y_pred, axis=1)
        return y_pred_sparsed

    @property
    def train_reporter(self) -> MetricsReporter:
        return self._train_reporter

    @property
    def val_reporter(self) -> MetricsReporter:
        return self._val_reporter

    @classmethod
    def create(cls, x_train, y_train, x_val, y_val):
        return cls(x_train, y_train, x_val, y_val)
