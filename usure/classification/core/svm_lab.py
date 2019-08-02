from typing import Iterable
import os
import numpy as np
from sklearn import svm
from .classifier_input import ClassifierInput
from .classifier_lab import ClassifierLab
np.random.seed(5)


class SvmLab(ClassifierLab):

    def __init__(self, input:ClassifierInput):
        super().__init__(input)

    @property
    def name(self):
        return "Svm"

    def research(self):

        input = self._input
        x_train, x_val, y_train, y_val = input.train_val_split(input.x_mean, input.y)


        clf = svm.LinearSVC()
        clf.fit(x_train, y_train)

        y_train_pred = clf.predict(x_train)
        y_val_pred = clf.predict(x_val)

        self._train_report.add_calculation(y_train_pred, XXXXX)
        self._validation_report.add_calculation(y_val_pred, XXXXX)
