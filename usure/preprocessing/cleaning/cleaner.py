from abc import ABCMeta, abstractmethod


class Cleaner:
    __metaclass__ = ABCMeta

    @abstractmethod
    def clean(self, text: str) -> str:
        raise NotImplementedError