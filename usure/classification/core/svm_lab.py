from typing import Iterable
import os
import numpy as np
from sklearn import svm
from .classifier_input import ClassifierInput
from .classifier_lab import ClassifierLab
from .metrics_reporter import MetricsReporter
from .model_dao import ModelDao
#np.random.seed(5)


class SvmLab(ClassifierLab):

    def __init__(self, input:ClassifierInput, dao:ModelDao):
        super().__init__(input, dao)

    @property
    def name(self):
        return f"svm-{self._input.embeddings_name}.skl"

    def research(self):

        input = self._input
        x_train, x_val, y_train, y_val = input.train_val_split(input.x_mean, input.y)

        clf = svm.SVC(kernel='rbf', gamma=0.9, C = 1, degree = 2, decision_function_shape='ova', probability=True)
    
        clf.fit(x_train, y_train)

        y_train_pred = clf.predict(x_train)
        y_train_pred_proba = clf.predict_proba(x_train)

        y_val_pred = clf.predict(x_val)
        y_val_pred_proba = clf.predict_proba(x_val)

        self._train_report = MetricsReporter.create(y_train, input.categories)
        self._validation_report = MetricsReporter.create(y_val, input.categories)

        self._train_report.add_calculation(y_train_pred, y_train_pred_proba)
        self._validation_report.add_calculation(y_val_pred, y_val_pred_proba)

        self._dao.save_sklearn(self.name, clf)
        #https://www.pyimagesearch.com/2016/09/05/multi-class-svm-loss/