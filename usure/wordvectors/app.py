from usure.config import config
import usure.common.logging as usurelogging
from usure.wordvectors.core import EmbeddingsMachine
from usure.wordvectors.infrastructure import FileCorpusRepository, FileKeyedVectorsRepository, FileWord2VecRepository


if __name__ == "__main__":

    usurelogging.config(config.logs, "wordvectors.log")

    corpusrep = FileCorpusRepository(config.preprocessed)

    w2vrep = FileWord2VecRepository(config.embeddings)

    kvsrep = FileKeyedVectorsRepository(config.embeddings)

    machine = EmbeddingsMachine(corpusrep, w2vrep, kvsrep)

    machine.init_work()
