from typing import Dict, Iterable, Any


class WordVectors:

    def __init__(self, name: str, vector_size, wordvectors: Dict[str, Iterable[Any]]):
        self._name = name
        self._wordvectors = wordvectors
        self._vector_size = vector_size

    @property
    def name(self) -> str:
        return self._name

    @property
    def vector_size(self):
        return self._vector_size

    @property
    def wordvectors(self) -> Dict[str, Iterable[Any]]:
        return self._wordvectors
