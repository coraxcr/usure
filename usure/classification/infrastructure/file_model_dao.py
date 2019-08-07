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
        name = f"{name}.h5"
        fullpath = fileutils.join(self._folderpath, name)
        model.save(fullpath, overwrite=True)

    def get_keras(self, name:str) -> Model:
        name = f"{name}.h5"
        fullpath = fileutils.join(self._folderpath, name)
        model = load_model(fullpath, compile=True)
        return model

    def save_keras_weights(self, name:str, model:Model):
        name = f"{name}.hdf5"
        fullpath = fileutils.join(self._folderpath, name)
        model.save_weights(fullpath, overwrite=True)

    def get_keras_weights(self, name:str, model:Model):
        name = f"{name}.hdf5"
        fullpath = fileutils.join(self._folderpath, name)
        model.load_weights(fullpath)
        return model

    def save_sklearn(self, name:str, model:SVC):
        name = f"{name}.joblib"
        fullpath = fileutils.join(self._folderpath, name)
        joblib.dump(model, fullpath) 

    def get_sklearn(self, name:str) -> SVC:
        name = f"{name}.joblib"
        fullpath = fileutils.join(self._folderpath, name)
        model = joblib.load(fullpath)
        return model