from usure.wordvectors.core import CorpusRep, Word2VecRep, KeyedVectorsRep, Corpus
from .vectorizer import Vectorizer


class EmbeddingsMachine:

    def __init__(self, corpusrep: CorpusRep,
                 w2vrep: Word2VecRep, kvsrep: KeyedVectorsRep):

        self._corpusrep = corpusrep

        self._w2vrep = w2vrep

        self._kvsrep = kvsrep

        self._vectorizers = [

            lambda corpus: Vectorizer.create_with_window(corpus, 1),
            lambda corpus: Vectorizer.create_with_window(corpus, 2),
            lambda corpus: Vectorizer.create_with_window(corpus, 4),
            lambda corpus: Vectorizer.create_with_window(corpus, 6),
            lambda corpus: Vectorizer.create_with_window(corpus, 8),
            lambda corpus: Vectorizer.create_with_window(corpus, 10),
            lambda corpus: Vectorizer.create_with_window(corpus, 12),
            lambda corpus: Vectorizer.create_with_window(corpus, 14),
            lambda corpus: Vectorizer.create_with_window(corpus, 16),
            lambda corpus: Vectorizer.create_with_window(corpus, 18),
            lambda corpus: Vectorizer.create_with_window(corpus, 20),
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
