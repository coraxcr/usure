import usure.common.logging as usurelogging
from usure.config import config
from usure.classification.infrastructure import (
     BasicSentenceCleaner 
    ,FileLabeledCommentsDao
    ,FileWordVectorsRep)
from usure.classification.core import CNN1D


class App:

    def __init__(self):
        cleaner = BasicSentenceCleaner(config.assets)
        self._commentsdao = FileLabeledCommentsDao(config.classification, cleaner)
        self._wvrep = FileWordVectorsRep(config.embeddings)
    
    def do(self):
        labeledcomments = self._commentsdao.get("intertass-CR-train-tagged.xml")
        wv = self._wvrep.get("tweets.txt.usu.sw.kvs")
        cnn = CNN1D(labeledcomments, wv)
        cnn.work()

if __name__ == "__main__":
    usurelogging.config(config.logs, "classification.log")
    app = App()
    app.do()