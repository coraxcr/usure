import logging
import time
from gensim.models import Word2Vec
from usure.wordvectors.infrastructure import TrainingCorpusDAO, TrainingCorpus
import multiprocessing

def logtime(function_to_decorate):
    def decore_logtime(vectorizer):
        logging.info(f"Starting time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
        logging.info(f"Vocab size: {len(vectorizer.w2v.wv.vocab)}")
        function_to_decorate(vectorizer)
        logging.info(f"Finish time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    return decore_logtime    

class Vectorizer:

    def __init__(self, name, sentences:TrainingCorpus, w2v: Word2Vec):
        assert isinstance(w2v, Word2Vec), "It's not a Word2Vec." 
        self._name = name
        self._sentences = sentences
        self._w2v = w2v
        self._w2v.build_vocab(sentences = sentences)

    @classmethod
    def create_with_smallwindow(cls, sentences):
        w2v=Vectorizer.create_word2vec(5)
        return cls("sw", sentences, w2v)
    
    @classmethod 
    def create_with_bigwindow(cls, sentences):
        w2v=Vectorizer.create_word2vec(9)
        return cls("bw", sentences, w2v)

    @staticmethod
    def create_word2vec(window:int):
        w2v = Word2Vec(sg=1, hs=1, size=300, min_count=3, workers=multiprocessing.cpu_count(), window=window)
        return  w2v

    @property
    def name(self):
        return self._name

    @property
    def w2v(self)->TrainingCorpus:
        return self._w2v

    @property
    def sentences(self):
        return self._sentences

    @logtime
    def train(self):
        self._w2v.train(sentences=self._sentences, total_examples=self.w2v.corpus_count, epochs=15)
