from typing import Iterable

class LabeledComments:

    def __init__(self, name:str, comments:Iterable[str], labels:Iterable[any]):
        self._name = name
        self._comments = comments
        self._labels = labels
    
    @property
    def name(self):
        return self._name

    @property
    def comments(self):
        return self._comments
    
    @property 
    def labels(self):
        return self._labels

    def get_training(percentage = 80) -> LabeledComments:
        raise NotImplementedError()

    def get_dev(percentage = 10) -> LabeledComments:
        raise NotImplementedError()

    def get_test(percentage = 10) -> LabeledComments:
        raise NotImplementedError()
