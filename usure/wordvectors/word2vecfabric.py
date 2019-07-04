from multiprocessing import cpu_count
from gensim.models import Word2Vec


class Word2VecFabric:

    _size = 300
    
    _min_count = 3
    
    #equal to one to deterministic way
    _workers = cpu_count()
    
    _seed = 1

    #skip gram
    _sg = 1 

    #hierarchical softmax
    _hs = 1

    def _create(self, window):
        w2v = Word2Vec(sg=self._sg, hs=self._hs, size=self._size, min_count=self._min_count, workers=self._workers, window = window)
        return w2v       

    def create_smallwindow(self):
        w2v = self._create(5)
        return w2v
    
    def create_bigwindow(self):
        w2v = self._create(7)
        return w2v