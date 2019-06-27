from .corpus_dao import CorpusDAO
from pandas import DataFrame

class TestCorpusDAO(CorpusDAO):

    def get_corpus(self) -> DataFrame:
        return self._get_corpus("test.txt")

    def store_corpus(self, data):
        self._store_corpus("test", data)    

    def get_corpus_by_chunks(self) -> DataFrame:
        return self._get_corpus_by_chunks("test.txt")