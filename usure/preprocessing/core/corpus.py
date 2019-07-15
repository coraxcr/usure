from typing import Iterable, Callable 

class Corpus:

    def __init__(self, name:str, get_sentences:Callable[[], Iterable[str]]):
        self._name = name
        self._get_sentences = get_sentences

    @property
    def name(self) -> str:
        return self._name

    def __iter__(self): 
        for sentence in self._get_sentences():
            if sentence:
                yield sentence