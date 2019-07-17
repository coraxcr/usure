from typing import Dict, Iterable, Any


class WordVectors:

    def __init__(self, name: str, wordvectors: Dict[str, Iterable[Any]])
    self._name = name
    self._wordvectors = wordvectors

    @property
    def name(self) -> str:
        return self._name

    @property
    def wordvectors(self) -> Dict[str, Iterable[Any]]:
        return self._wordvectors
