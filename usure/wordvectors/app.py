from usure.config import config
import usure.common.logging as usurelogging
from usure.wordvectors.core import EmbeddingsMachine
from usure.wordvectors.infrastructure import FileCorpusRep, FileKeyedVectorsRep, FileWord2VecRep


if __name__ == "__main__":

    usurelogging.config(config.logs, "wordvectors.log")

    corpusrep = FileCorpusRep(config.preprocessed)

    w2vrep = FileWord2VecRep(config.embeddings)

    kvsrep = FileKeyedVectorsRep(config.embeddings)

    machine = EmbeddingsMachine(corpusrep, w2vrep, kvsrep)

    machine.init_work()
