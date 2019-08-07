import uuid
from abc import ABC, abstractmethod
from typing import Iterable, Any
import statistics
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold
from .classifier_input import ClassifierInput
from .metrics import Metrics
from .model_dao import ModelDao

class ModelReport:

    def __init__(self, name, training:Metrics, validation:Metrics):
        self._name = name
        self._training = training
        self._validation = validation
        self._epochs = []

    @classmethod
    def create(cls, name:str, training:Metrics, validation:Metrics):
        return cls(name, training, validation)

    @classmethod
    def create(cls, name, categories, predict, x_train, x_val, y_train, y_val):
        train_prediction = predict(x_train)
        val_prediction = predict(x_val)
        training_metrics = Metrics.create(y_train, train_prediction[0], train_prediction[1], categories)
        validation_metrics = Metrics.create(y_val, val_prediction[0], val_prediction[1], categories)
        return cls(name, training_metrics, validation_metrics)
        
    @property
    def name(self) -> str:
        return self._name

    @property
    def training(self) -> Metrics:
        return self._training

    @property
    def validation(self) -> Metrics:
        return self._validation

    @property
    def epochs(self) -> Iterable['ModelReport']:
        return self._epochs

    @epochs.setter
    def epochs(self, value:Iterable['ModelReport']):
        self._epochs = value


class LabReport:

    def __init__(self):
        self._model_reports = []

    @classmethod
    def create(cls):
        return cls()

    @property
    def model_reports(self) -> Iterable[ModelReport]:
        return self._model_reports

    @property 
    def summary(self) -> pd.DataFrame:
        summary = {
            "train_acc_mean" : [statistics.mean(list(map(lambda model_report: model_report.training.accuracy, self._model_reports)))],
            "train_acc_stdev" : [statistics.stdev(list(map(lambda model_report: model_report.training.accuracy, self._model_reports)))],           
            "val_acc_mean" : [statistics.mean(list(map(lambda model_report: model_report.validation.accuracy, self._model_reports)))],
            "val_acc_stdev" : [statistics.stdev(list(map(lambda model_report: model_report.validation.accuracy, self._model_reports)))]
        }
        return pd.DataFrame(summary)

    def add(self, model_report:ModelReport):
        self._model_reports.append(model_report)


class ClassifierLab:
    """Classifier Laboratory"""

    def __init__(self, dao: ModelDao):
        self._dao = dao

    @abstractmethod 
    def train_by_stratifiedkfold(self, input:ClassifierInput, folds=10) -> LabReport:
        pass
    
    @abstractmethod
    def create_model(self):
        pass

    @abstractmethod
    def test(self, model_name, test_input:ClassifierInput) -> Metrics:
        pass

    @abstractmethod
    def predict(self, model_name, input:ClassifierInput) -> Iterable[str]:
         pass

    def get_an_id(self):
        return uuid.uuid4().hex

    def train_val_split(self, x, y, val_size=0.1):
        return train_test_split(x, y, test_size=val_size, random_state=42, shuffle=True)

    def train_val_stratifiedkfold(self, x, y, folds=10):
        kf = StratifiedKFold(n_splits=folds, shuffle=True)
        for train_indexes, validation_indexes in kf.split(x, y):
            x_train, x_val = x[train_indexes], x[validation_indexes]
            y_train, y_val = y[train_indexes], y[validation_indexes]
            yield x_train, x_val, y_train, y_val