from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import log_loss
from sklearn.metrics import confusion_matrix
from typing import Iterable
import pandas as pd


class Metrics:

    def __init__(self, y_true, y_pred, raw_y_pred, categories):
        self._set_metrics(y_true, y_pred, raw_y_pred, categories)

    @property
    def accuracy(self) -> float:
        return self._accuracy
    
    @property
    def loss(self) -> float:
        return self._loss

    @property 
    def classification_report(self) ->str:
        return self._classification_report

    @property 
    def confusion_matrix(self) -> pd.DataFrame:
        return self._confusion_matrix

    def _set_metrics(self, y_true, y_pred, raw_y_pred, categories):
        self._accuracy = accuracy_score(y_true, y_pred)
        self._loss = log_loss(y_true, raw_y_pred)
        self._classification_report = classification_report(y_true, y_pred, target_names=categories)
        self._confusion_matrix = self._format_confusion_matrix(confusion_matrix(y_true, y_pred), categories)

    def _format_confusion_matrix(self, confusion_matrix, categories):
        df = pd.DataFrame(confusion_matrix)
        df.columns = categories
        df.insert(0, "Pred/True", categories)
        df.set_index('Pred/True',inplace=True)
        return df

    @classmethod
    def create(cls, y_true, y_pred, raw_y_pred, categories):
        return cls(y_true, y_pred, raw_y_pred, categories)
