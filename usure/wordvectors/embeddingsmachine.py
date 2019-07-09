from usure.wordvectors.infrastructure import TrainingCorpusDAO, Word2VecDAO, TrainingCorpus, TrainingCorpora
from .vectorizer import Vectorizer
from gensim.models import Word2Vec
import time 

class EmbeddingsMachine:

    def __init__(self, corpus_dao:TrainingCorpusDAO, w2v_dao:Word2VecDAO):
        self._corpus_dao = corpus_dao
        self._w2v_dao = w2v_dao
        self._vectorizers =  [
            lambda corpus_dao: Vectorizer.create_with_smallwindow(corpus_dao),
            lambda corpus_dao: Vectorizer.create_with_bigwindow(corpus_dao)
        ]

    def init_work(self):
        corpora = self._corpus_dao.get_trainingcorpora()
        for corpus in corpora:
            self._create_embeddings(corpus)
    
    def _create_embeddings(self, corpus:TrainingCorpus):
        for create_vectorizer in self._vectorizers:
            vectorizer = create_vectorizer(corpus)
            vectorizer.train()
            self._save(vectorizer)

    def _save(self, vectorizer:Vectorizer):
        self._w2v_dao.save_model(vectorizer)