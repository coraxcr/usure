import usure.common.logging as usurelogging
from usure.config import config
from usure.classification.infrastructure import (
     BasicSentenceCleaner 
    ,FileLabeledCommentsDao
    ,FileWordVectorsRep)
from usure.classification.core import CnnLab, SvmLab, ClassifierInput


class App:

    def __init__(self):
        cleaner = BasicSentenceCleaner(config.assets)
        self._commentsdao = FileLabeledCommentsDao(config.classification, cleaner)
        self._wvrep = FileWordVectorsRep(config.embeddings)
    
    def do(self):
        labeledcomments = self._commentsdao.get("intertass-CR-train-tagged.xml")

        wv = self._wvrep.get("CorpusFBCR2013.txt.usu.bw.kvs")
        #wvs = self._wvrep.get_all()
        #for wv in wvs:
        clasifier = CnnLab(ClassifierInput(labeledcomments, wv))

if __name__ == "__main__":
    usurelogging.config(config.logs, "classification.log")
    app = App()
    app.do()