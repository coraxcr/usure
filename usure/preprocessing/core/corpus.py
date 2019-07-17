from typing import Iterator, Callable


class Corpus:

    def __init__(self, name: str, get_sentences: Callable[[], Iterator[str]]):
        self._name = name
        self._get_sentences = get_sentences

    @property
    def name(self) -> str:
        return self._name

    def __iter__(self) -> Iterator[str]:
        return self._get_sentences()
