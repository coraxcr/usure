import usure.common.logging as usurelogging
from usure.config import config
from usure.classification.infrastructure import (
     BasicSentenceCleaner 
    ,FileLabeledCommentsDao
    ,FileWordVectorsRep)
from usure.classification.core import CnnLab, SvmLab, ClassifierInput
from usure.classification.ui import utils
from usure.classification.infrastructure import FileModelDao

class AppCrossValidation:

    def __init__(self):
        cleaner = BasicSentenceCleaner(config.assets)
        self._commentsdao = FileLabeledCommentsDao(config.classification, cleaner)
        self._wvrep = FileWordVectorsRep(config.embeddings)
        self._modeldao = FileModelDao(config.models)
    
    def execute(self):
        trainingset = self._commentsdao.get("intertass-CR-train-tagged.xml")
        wordvectors = self._wvrep.get("CorpusFBCR2013.txt.usu.bw.kvs")
        input = ClassifierInput(trainingset, wordvectors)
        
        #wvs = self._wvrep.get_all()
        #for wv in wvs:
        classifier = CnnLab(input, self._modeldao)
        utils.print_metrics(classifier.train_report, classifier.validation_report, only_last=True)

if __name__ == "__main__":
    usurelogging.config(config.logs, "classification.log")
    app = AppCrossValidation()
    app.execute()