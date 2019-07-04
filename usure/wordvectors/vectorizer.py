from gensim.models import Word2Vec
from usure.wordvectors.infrastructure import TrainingCorpusDAO

class Vectorizer:

    def __init__(self, dao: TrainingCorpusDAO, w2v: Word2Vec):
        self._dao = dao
        self._w2v = w2v

    @property
    def dao(self):
        return self._dao

    @dao.setter
    def dao(self, value):
        assert isinstance(value, TrainingCorpusDAO), "It's not a DAO."
        self._dao = value

    @property
    def w2v(self):
        return self._w2v

    @w2v.setter
    def w2v(self, value):
        assert isinstance(value, Word2Vec), "It's not a Word2Vec." 
        self._w2v = value

    def feed(self):
        sentences = self._dao.get_trainingcorpus()
        self._w2v.build_vocab(sentences = sentences)

    def train(self):
        sentences = self._dao.get_trainingcorpus()
        self._w2v.train(sentences= sentences, total_examples= self.w2v.corpus_count, epochs=15)#self.w2v.epochs