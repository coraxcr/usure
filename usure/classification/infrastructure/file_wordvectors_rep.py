from gensim.models import KeyedVectors
from usure.classification.core import WordVectors, WordVectorsRepository
from usure.wordvectors.infrastructure import FileKeyedVectorsRepository


class FileWordVectorsRep(WordVectorsRep):

    def __init__(self, folderpath:str):
        self._kvsrep = FileKeyedVectorsRepository(folderpath)

    def get(self,name:str) -> WordVectors:
        kvs = self._kvsrep.get(name)
        wvs = self._from_kvs_to_wvs(kvs)
        return wvs

    def get_all(self) -> Iterable[WordVectors]:
        kvs = self._keyedvectordao.get_all()
        wsvs = map(self._from_kvs_to_wvs, kvs)
        return wsvs

    def _from_kvs_to_wvs(self, kvs:KeyedVectors) -> WordVectors:
        wvs = WordVectors(kvs.name, { word : kvs.get_vector(word) for word, vocab in kvs.wv.items() })
        return wvs   