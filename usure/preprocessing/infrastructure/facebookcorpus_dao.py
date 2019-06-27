from .corpus_dao import CorpusDAO
from pandas import DataFrame

class FacebookCorpusDAO(CorpusDAO):

    def get_corpus(self) -> DataFrame:
        return self._get_corpus("CorpusFBCR2013.txt")

    def store_corpus(self, data):
        self._store_corpus("CorpusFBCR2013", data)

    def get_corpus_by_chunks(self):
        return self._get_corpus_by_chunks("CorpusFBCR2013.txt")
    