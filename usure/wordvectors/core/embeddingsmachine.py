from gensim.models import Word2Vec
from usure.wordvectors.core import CorpusRepository, Word2VecRepository, KeyedVectorsRepository, Corpus
from .vectorizer import Vectorizer


class EmbeddingsMachine:

    def __init__(self, corpusrep: CorpusRepository,
                 w2vrep: Word2VecRepository, kvsrep: KeyedVectorsRepository):

        self._corpusrep = corpusrep

        self._w2vrep = w2vrep

        self._kvsrep = kvsrep

        self._vectorizers = [

            lambda corpus: Vectorizer.create_with_smallwindow(corpus),

            lambda corpus: Vectorizer.create_with_bigwindow(corpus)
        ]

    def init_work(self):

        corpora = self._corpusrep.get_all()

        for corpus in corpora:

            self._create_embeddings(corpus)

    def _create_embeddings(self, corpus: Corpus):

        for create_vectorizer in self._vectorizers:

            vectorizer = create_vectorizer(corpus)

            vectorizer.train()

            self._save(vectorizer)

    def _save(self, vectorizer: Vectorizer):

        self._w2vrep.save(vectorizer.w2v)

        self._kvsrep.save(vectorizer.w2v.wv)
