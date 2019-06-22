from abc import ABC, abstractmethod 
from .cleaningtask import CleaningTask


class CleaningTaskFactory(ABC):

    @abstractmethod
    def create_basic_process(self) -> CleaningTask:
        raise NotImplementedError 