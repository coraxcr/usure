import multiprocessing
from gensim.models import Word2Vec
from usure.wordvectors.core import CorpusRepository, Corpus
from usure.common import logging


class Vectorizer:

    def __init__(self, typename, corpus: Corpus, w2v: Word2Vec):
        assert isinstance(w2v, Word2Vec), "It's not a Word2Vec."
        self._typename = typename
        self._corpus = corpus
        self._w2v = w2v
        self._w2v.build_vocab(sentences=corpus)
        self._w2v.name = f"{corpus.name}.{self._typename}.w2v"
        self._w2v.wv.name = f"{corpus.name}.{self._typename}.kvs"

    @classmethod
    def create_with_smallwindow(cls, corpus):
        w2v = Vectorizer.create_word2vec(5)
        return cls("sw", corpus, w2v)

    @classmethod
    def create_with_bigwindow(cls, corpus):
        w2v = Vectorizer.create_word2vec(9)
        return cls("bw", corpus, w2v)

    @staticmethod
    def create_word2vec(window: int):
        w2v = Word2Vec(
            sg=1,
            hs=1,
            size=300,
            min_count=3,
            workers=multiprocessing.cpu_count(),
            window=window)

        return w2v

    @property
    def typename(self):
        return self._typename

    @property
    def w2v(self) -> Word2Vec:
        return self._w2v

    @property
    def corpus(self):
        return self._corpus

    @logging.logtime
    def train(self):

        logging.info_time(f"CREATING EMBEDDINGS FOR CORPUS: {self.w2v.name}")

        self._w2v.train(
            sentences=self._corpus,
            total_examples=self.w2v.corpus_count,
            epochs=15)
