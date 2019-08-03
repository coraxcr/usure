from keras.models import Model
from keras.models import load_model
from sklearn.svm import SVC
from sklearn.externals import joblib
from usure.classification.core import ModelDao
from usure.common import fileutils


class FileModelDao(ModelDao):

    def __init__(self, folderpath: str):
        self._folderpath = folderpath

    def save_keras(self, name:str, model:Model):
        fullpath = fileutils.join(self._folderpath, name)
        model.save(fullpath, overwrite=True)

    def save_sklearn(self, name:str, model:SVC):
        fullpath = fileutils.join(self._folderpath, name)
        joblib.dump(model, fullpath) 


    def get_keras(self, name:str) -> Model:
        fullpath = fileutils.join(self._folderpath, name)
        model = load_model(fullpath, compile=True)
        return model

    def get_sklearn(self, name:str) -> SVC:
        fullpath = fileutils.join(self._folderpath, name)
        model = joblib.load(fullpath)
        return model