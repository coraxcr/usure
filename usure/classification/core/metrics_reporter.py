from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import log_loss
from sklearn.metrics import confusion_matrix


class MetricsReporter:

    def __init__(self, y_true, categories = None):
        self._y_true = y_true
        self._categories = categories
        self._accuracies = []
        self._losses =[]
        self._classification_reports = []
        self._confusion_matrices = []

    @property
    def categories(self):
        return self._categories

    @property
    def accuracies(self):
        return self._accuracies
    
    @property
    def losses(self):
        return self._losses

    @property 
    def classification_reports(self):
        return self._classification_reports

    @property 
    def confusion_matrices(self):
        return self._confusion_matrices

    def add_calculation(self, y_pred, raw_y_pred):
        self._accuracies.append(accuracy_score(self._y_true, y_pred)),
        self._losses.append(log_loss(self._y_true, raw_y_pred))
        self._classification_reports.append(classification_report(self._y_true, y_pred, target_names=self._categories))
        self._confusion_matrices.append(confusion_matrix(self._y_true, y_pred))

    @classmethod
    def create(cls, y_true, class_names):
        return cls(y_true, class_names)

    #(float_format=lambda n: format(n, '#.2g'), justify="right")
