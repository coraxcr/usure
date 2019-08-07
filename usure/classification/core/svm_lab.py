from typing import Iterable, Any
import os
import numpy as np
from sklearn import svm
from .classifier_input import ClassifierInput
from .classifier_lab import ClassifierLab, LabReport, ModelReport, ModelDao
from .metrics import Metrics


class SvmLab(ClassifierLab):

    def __init__(self, dao:ModelDao):
        super().__init__(dao)

    def train_by_stratifiedkfold(self, input:ClassifierInput, folds=10) -> LabReport:   
        labreport = LabReport.create() 
        for x_train, x_val, y_train, y_val in self.train_val_stratifiedkfold(input.x_vectorized_mean, input.y_indexes, folds=folds):
            model = self.create_model()
            modelname = self.get_an_id()
            model.fit(x_train, y_train)
            model_report = ModelReport.create(modelname, 
                input.categories,
                lambda x: self._predict(x, model),
                x_train, x_val, y_train, y_val)
            labreport.add(model_report)
            self._dao.save_sklearn(modelname, model)
        return labreport

    def create_model(self):
        model = svm.SVC(kernel='rbf', gamma=0.4, C = 0.7, degree = 2, decision_function_shape='ova', probability=True)
        return model

    def test(self, model_name, test_input:ClassifierInput) -> Metrics:
        model = self._dao.get_sklearn(model_name)
        y_pred_sparsed, y_pred = self._predict(test_input.x_vectorized_mean, model)
        metrics = Metrics.create(test_input.y_indexes, y_pred_sparsed, y_pred, test_input.categories)
        return metrics

    def predict(self, model_name, input:ClassifierInput) -> Iterable[str]:
        model = self._dao.get_sklearn(model_name)
        y_pred_sparsed, y_pred = _predict(input.x_vectorized_mean, model)
        labeled_predictions = np.array([input.categories[index] for index in y_pred_sparsed], dtype=object)
        return labeled_predictions
    
    def _predict(self, x, model:svm.SVC):
        y_pred =  model.predict_proba(x)
        y_pred_sparsed = model.predict(x)
        return y_pred_sparsed, y_pred