from usure.classification.core import KeyedVectorsRep
from usure.wordvectors.infrastructure import KeyedVectorsDAO

class FileKeyedVectorsRep(KeyedVectorsRep):

    def __init__(self):
        self._keyedvectordao = KeyedVectorsDAO()

    def get(self,name:str) -> KeyedVectors:
        return self._keyedvectordao.get(name)

    def get_all(self) -> Iterable[KeyedVectors]:
        return self._keyedvectordao.get_all()

