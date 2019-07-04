from gensim.models import Word2Vec
from usure.wordvectors.infrastructure import Word2VecDAO

class FbWord2VecDAO(Word2VecDAO):

    def __init__(self):
        super().__init__()
        self._fullfilepath = self._get_absolute_path("CorpusFBCR2013.w7.w2v")