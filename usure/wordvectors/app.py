import logging
import time 
import os
from os.path import join
from usure.wordvectors.embeddingsmachine import EmbeddingsMachine
from usure.wordvectors.infrastructure import TrainingCorpusDAO, Word2VecDAO

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(join(location,"infrastructure","assets","corpora","logs","wordvectors.log"))
        ,logging.StreamHandler()
        ]
)

if __name__ == "__main__":
    corpus_dao = TrainingCorpusDAO()
    w2v_dao = Word2VecDAO()
    machine = EmbeddingsMachine(corpus_dao, w2v_dao)
    machine.init_work()