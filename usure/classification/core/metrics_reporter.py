from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from keras.callbacks import Callback
import numpy as np
import pandas as pd

class MetricsReporter:

    def __init__(self, y_true):
        self._y_true = y_true
        self._metrics = pd.DataFrame(columns=[
             "accuracy"
            ,"precision"
            ,"recall"
        ]
        )

    def add_calculation(self, y_pred):
        metrics = {
            "accuracy" : accuracy_score(self._y_true, y_pred),
            "precision" : precision_score(self._y_true, y_pred, average="micro"),
            "recall": recall_score(self._y_true, y_pred, average="micro")
        }
        self._metrics = self._metrics.append(metrics, ignore_index=True)

    def to_string(self):
        return self._metrics.to_string(float_format=lambda n: format(n, '#.2g'), justify="right")

    @classmethod
    def create(cls, y_true):
        return cls(y_true)
