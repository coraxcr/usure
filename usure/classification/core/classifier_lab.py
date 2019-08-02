from abc import ABC, abstractmethod
from .classifier_input import ClassifierInput
from .metrics_reporter import MetricsReporter


class ClassifierLab:
    """Classifier Laboratory"""

    def __init__(self, input:ClassifierInput):
        self._input = input
        self._train_report = None
        self._validation_report = None
        self.research()

    @abstractmethod
    def research(self):
        pass
        
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    def train_report(self) -> MetricsReporter:
        return self._train_report

    @property
    def validation_report(self) -> MetricsReporter:
        return self._validation_report

