import multiprocessing
from gensim.models import Word2Vec
from usure.wordvectors.core import CorpusRep, Corpus
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
    def create_with_window(cls, corpus, max_skip_len):
        w2v = Vectorizer.create_word2vec(max_skip_len)
        return cls(f"{max_skip_len}_w", corpus, w2v)

    @staticmethod
    def create_word2vec(window: int):
        w2v = Word2Vec(
            negative = 10,
            sg=1,
            hs=0,
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
            epochs=5)
