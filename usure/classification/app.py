import usure.common.logging as usurelogging
from usure.config import config
from usure.classification.infrastructure import (
     BasicSentenceCleaner 
    ,FileLabeledCommentsDao
    ,FileWordVectorsRep)
from usure.classification.core import CnnLab, SvmLab, ClassifierInput, LabReport
from usure.classification.infrastructure import FileModelDao
import usure.classification.ui.utils as ui

class App:

    def __init__(self):
        cleaner = BasicSentenceCleaner(config.assets)
        self._commentsdao = FileLabeledCommentsDao(config.classification, cleaner)
        self._wvrep = FileWordVectorsRep(config.embeddings)
    
    def do(self):
        labeledcomments = self._commentsdao.get("intertass-CR-train-tagged.xml") #intertass-CR-test

        wv = self._wvrep.get("CorpusFBCR2013.txt.usu.sw.kvs")
        input = ClassifierInput(labeledcomments, wv)
        model_dao = FileModelDao(config.models)
        lab = CnnLab(input, model_dao)
        labreport = lab.train_by_stratifiedkfold()
        print(labreport.summary.to_string())
        df = ui.model_reports_to_DataFrame(labreport.model_reports)
        print(df.to_string())
        
        #metrics = lab.test("020863a7b1ef4ba1a3e95e91d2d0dd51", input)
        #print(metrics.accuracy)

if __name__ == "__main__":
    usurelogging.config(config.logs, "classification.log")
    app = App()
    app.do()