from abc import ABC, abstractclassmethod
from keras.models import Model
from sklearn.svm import SVC

class ModelDao:

    @abstractclassmethod
    def save_keras(name:str, model:Model):
        pass

    @abstractclassmethod
    def save_sklearn(name:str, model:SVC):
        pass

    @abstractclassmethod
    def get_keras(name:str) -> Model:
        pass

    @abstractclassmethod
    def get_sklearn(name:str) -> SVC:
        pass