from typing import Iterable

class LabeledComments:

    def __init__(self, name:str, comments:Iterable[str], labels:Iterable[any]):
        assert len(comments) == len(labels), "Lenght of comments and labels are not the same."
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

    @property
    def count(self):
        return len(self._comments)
            

