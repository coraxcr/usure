from usure.wordvectors.infrastructure import FbTrainingCorpusDAO, TwitterTrainingCorpusDAO
from .word2vecfabric import Word2VecFabric
from .vectorizer import Vectorizer


class VectorizerFabric:

    _fbtrainingcorpusdao = FbTrainingCorpusDAO()
    _twittertrainingcorpusdao = TwitterTrainingCorpusDAO()
    _word2vecfabric = Word2VecFabric()

    def create_fb_smallwindow(self):
        vectorizer = Vectorizer(self._fbtrainingcorpusdao, self._word2vecfabric.create_smallwindow())
        return vectorizer

    def create_fb_bigwindow(self):
        vectorizer = Vectorizer(self._fbtrainingcorpusdao, self._word2vecfabric.create_bigwindow())
        return vectorizer

    def create_twitter_smallwindow(self):
        vectorizer = Vectorizer(self._twittertrainingcorpusdao, self._word2vecfabric.create_smallwindow())
        return vectorizer

    def create_twitter_bigwindow(self):
        vectorizer = Vectorizer(self._twittertrainingcorpusdao, self._word2vecfabric.create_bigwindow())
        return vectorizer
