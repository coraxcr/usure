import usure.common.logging as usurelogging
from usure.config import config
from usure.classification.infrastructure import (
     BasicSentenceCleaner 
    ,FileLabeledCommentsDao
    ,CsvLabeledCommentsDao
    ,FileWordVectorsRep)
from usure.classification.core import CnnLab, SvmLab, ClassifierInput, LabReport, WordVectorsService
from usure.classification.infrastructure import FileModelDao
import usure.classification.ui.utils as ui


class App:

    def __init__(self):
        cleaner = BasicSentenceCleaner(config.assets)
        self._commentsdao = CsvLabeledCommentsDao(config.sets, cleaner)
        self._wvrep = FileWordVectorsRep(config.embeddings)
    
    def do(self):
        labeledcomments = self._commentsdao.get("train.csv") #intertass-CR-test
        wv = self._wvrep.get("CorpusFBCR2013.txt.usu.sw.kvs")
        wv_service = WordVectorsService(wv)
        input = ClassifierInput(labeledcomments, wv_service)
        model_dao = FileModelDao(config.models)
        lab = SvmLab(model_dao)
        #labreport = lab.train_by_stratifiedkfold(input)
        #print(labreport.summary.to_string())
        #df = ui.model_reports_to_DataFrame(labreport.model_reports)
        #print(df.to_string())
        #metrics = lab.test("0a437e7ad5194d0788dd2123af7e1f31", input)
        #print(metrics.accuracy)
        result = lab.optimization(input)
        print(result)

if __name__ == "__main__":
    usurelogging.config(config.logs, "classification.log")
    app = App()
    app.do()