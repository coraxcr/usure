from usure.classification.core import WordVectorsRep
from usure.wordvectors.infrastructure import KeyedVectorsDAO
from usure.classification.core.models import WordVectors
from gensim.models import KeyedVectors


class FileWordVectorsRep(WordVectorsRep):

    def __init__(self):
        self._keyedvectorsdao = KeyedVectorsDAO()

    def get(self,name:str) -> WordVectors:
        kvs = self._keyedvectorsdao.get(name)
        wvs = self._from_kvs_to_wvs(kvs)
        return wvs

    def get_all(self) -> Iterable[WordVectors]:
        kvs = self._keyedvectordao.get_all()
        wsvs = map(self._from_kvs_to_wvs, kvs)
        return wsvs

    def _from_kvs_to_wvs(self, kvs:KeyedVectors) -> WordVectors:
        wvs = WordVectors(kvs.name, { word : kvs.get_vector(word) for word, vocab in kvs.vocab.items() })
        return wvs        
