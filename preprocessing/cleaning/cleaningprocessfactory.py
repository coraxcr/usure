from abc import ABC, abstractmethod 
from .cleaningprocess import CleaningProcess


class CleaningProcessFactory(ABC):

    @abstractmethod
    def create_basic_process(self) -> CleaningProcess:
        raise NotImplementedError 