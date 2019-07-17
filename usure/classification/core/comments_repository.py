from abc import ABC, abstractmethod

class CommentsRepository(ABC):

    @abstractmethod
    def get_training(self):
        pass

    def get_dev(self):
        pass

    def get_test(self):
        pass