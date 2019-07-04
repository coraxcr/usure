from gensim.models import Word2Vec
from usure.wordvectors.infrastructure import Word2VecDAO

class TwitterWord2VecDAO(Word2VecDAO):

    def __init__(self):
        super().__init__()
        self._fullfilepath = self._get_absolute_path("twitter.w2.w2v")