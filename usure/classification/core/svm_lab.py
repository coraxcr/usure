from typing import Iterable, Any
import os
import numpy as np
from sklearn import svm
from .classifier_input import ClassifierInput
from .classifier_lab import ClassifierLab, LabReport, ModelReport
from .metrics import Metrics
from .model_dao import ModelDao
#np.random.seed(5)


class SvmLab(ClassifierLab):

    def __init__(self, input:ClassifierInput, dao:ModelDao):
        super().__init__(input, dao)

    def train_by_stratifiedkfold(self, folds=10) -> LabReport:
        input = self._input       
        labreport = LabReport.create() 
        for x_train, x_val, y_train, y_val in input.train_val_stratifiedkfold(input.x, input.y, folds=folds):
            model = self.create_model(input)
            modelname = self.get_an_id()
            model.fit(x_train, y_train)
            model_report = ModelReport.create(modelname, 
                input.categories,
                lambda x: self._predict(x, model),
                x_train, x_val, y_train, y_val)
            labreport.add(model_report)
            self._dao.save_sklearn(modelname, model)

        return labreport

    def test(self, modelname:str, input:ClassifierInput) -> Metrics:
        model = self._dao.get_sklearn(modelname)
        y_pred_sparsed, y_pred = _predict(input.x, model)
        metrics = Metrics.create(input.y, y_pred_sparsed, y_pred, input.categories)
        return metrics

    def predict(self, modelname, input:ClassifierInput) -> Iterable[Any]:
        model = self._dao.get_sklearn(modelname)
        y_pred_sparsed, y_pred = _predict(input.x, model)
        labeled_predictions = np.array([input.categories[index] for index in y_pred_sparsed], dtype=object)
        return labeled_predictions
    
    def _predict(self, x, model:svm.SVC):
        y_pred =  model.predict_proba(x)
        y_pred_sparsed = model.predict(x)
        return y_pred_sparsed, y_pred

    def create_model(self, input:ClassifierInput):
        model = svm.SVC(kernel='rbf', gamma=0.4, C = 0.7, degree = 2, decision_function_shape='ova', probability=True)
        return model