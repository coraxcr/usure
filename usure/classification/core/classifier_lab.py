from abc import ABC, abstractmethod
from typing import Iterable
import statistics
import pandas as pd
from .classifier_input import ClassifierInput
from .metrics import Metrics
from .model_dao import ModelDao


class LabReport:

    def __init__(self):
        self._model_names = []
        self._trainings = []
        self._validations = []

    @classmethod
    def create(cls):
        return cls()
        
    @property
    def model_names(self) -> Iterable[str]:
        return self._model_names

    @property
    def trainings(self) -> Iterable[Metrics]:
        return self._trainings

    @property
    def validations(self) -> Iterable[Metrics]:
        return self._validations

    @property 
    def sumary(self) -> pd.DataFrame:
        sumary = {
            "tra_acc_mean" : [statistics.mean(list(map(lambda metrics: metrics.accuracy, self._trainings)))],
            "val_acc_mean" : [statistics.mean(list(map(lambda metrics: metrics.accuracy, self._validations)))],
            "tra_acc_variance" : [statistics.variance(list(map(lambda metrics: metrics.accuracy, self._trainings)))],
            "val_acc_variance" : [statistics.variance(list(map(lambda metrics: metrics.accuracy, self._validations)))]
        }
        return pd.DataFrame(sumary)

    def add(self, model_name, training_metrics:Metrics, validation_metrics:Metrics):
        self._model_names.append(model_name)
        self._trainings.append(training_metrics)
        self._validations.append(validation_metrics)


class ClassifierLab:
    """Classifier Laboratory"""

    def __init__(self, input:ClassifierInput, dao: ModelDao):
        self._input = input
        self._dao = dao

    @abstractmethod 
    def train_by_stratifiedkfold() -> LabReport:
        pass
