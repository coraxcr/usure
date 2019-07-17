from abc import ABC, abstractmethod


class SentenceCleaner(ABC):

    @abstractmethod
    def clean(text: str) -> str:
        pass
