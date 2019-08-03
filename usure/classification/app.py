import usure.common.logging as usurelogging
from usure.config import config
from usure.classification.infrastructure import (
     BasicSentenceCleaner 
    ,FileLabeledCommentsDao
    ,FileWordVectorsRep)
from usure.classification.core import CnnLab, ClassifierInput, LabReport
#from usure.classification.ui import utils
from usure.classification.infrastructure import FileModelDao


class App:

    def __init__(self):
        cleaner = BasicSentenceCleaner(config.assets)
        self._commentsdao = FileLabeledCommentsDao(config.classification, cleaner)
        self._wvrep = FileWordVectorsRep(config.embeddings)
    
    def do(self):
        labeledcomments = self._commentsdao.get("intertass-CR-train-tagged.xml")

        wv = self._wvrep.get("tweets.txt.usu.sw.kvs")
        input = ClassifierInput(labeledcomments, wv)
        dao = FileModelDao(config.models)
        #wvs = self._wvrep.get_all()
        #for wv in wvs:
        lab = CnnLab(input, dao)
        labreport = lab.train_by_stratifiedkfold()
        print(labreport.sumary.to_string())

if __name__ == "__main__":
    usurelogging.config(config.logs, "classification.log")
    app = App()
    app.do()