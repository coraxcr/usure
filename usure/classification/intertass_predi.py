from usure.config import config
import usure.common.logging as usurelogging
from typing import List 
from usure.classification.core import (CnnLab, 
    SvmLab, 
    LabeledComments,
    LabeledCommentsDao,
    ClassifierInput,
    WordVectorsService,
    ModelDao)
from usure.classification.infrastructure import(
    FileModelDao,
    FileLabeledCommentsDao,
    BasicSentenceCleaner,
    FileWordVectorsRep
)

class IntertassPred:
    """Intertass preddictor"""
     
    def __init__(self, 
            cnn_lab:CnnLab,
            svm_lab:SvmLab,
            comments_dao:LabeledCommentsDao):
        self._cnn_lab = cnn_lab
        self._svm_lab = svm_lab
        self._comments_dao = comments_dao
        self._categories = ['N', 'NEU', 'NONE', 'P']

    def predict_unlabeled_comments_and_save(self, 
        comments_name: str,
        cnn_model_name:str, 
        svm_model_name:str, 
        wv_service:WordVectorsService):

        comments = self._comments_dao.get(comments_name)

        input = ClassifierInput(comments, wv_service, self._categories)

        cnn_prediction = self._cnn_lab.predict(cnn_model_name, input)
        svm_prediction = self._svm_lab.predict(svm_model_name, input)

        cnn_comment_result = LabeledComments(f"{cnn_model_name}-{wv_service.name}.cnn.xml", comments.comments, cnn_prediction)
        svm_comment_result = LabeledComments(f"{svm_model_name}-{wv_service.name}.svm.xml", comments.comments, svm_prediction)

        self._comments_dao.save_from_origin(cnn_comment_result, comments_name)
        self._comments_dao.save_from_origin(svm_comment_result, comments_name)
      
        
if __name__ == "__main__":

    model_dao = FileModelDao(config.models)
    cnn_lab = CnnLab(model_dao)
    svm_lab = SvmLab(model_dao)
    sentence_cleaner = BasicSentenceCleaner(config.assets)
    comments_dao = FileLabeledCommentsDao(config.classification, sentence_cleaner)
    pred = IntertassPred(cnn_lab, svm_lab, comments_dao)   
    wv_rep = FileWordVectorsRep(config.embeddings)


    ## FB BW
    wv_service = WordVectorsService(wv_rep.get("CorpusFBCR2013.txt.usu.bw.kvs"))
    pred.predict_unlabeled_comments_and_save(
        "intertass-CR-test.xml",
        "12c9f5f4a0ee47b6be4357d22cfd8d4c",
        "bf8b2648647a4090b179c326c3caf972", 
        wv_service)
    ##    
    ## FB SW
    wv_service = WordVectorsService(wv_rep.get("CorpusFBCR2013.txt.usu.sw.kvs"))
    pred.predict_unlabeled_comments_and_save(
        "intertass-CR-test.xml",
        "df884a4b4bd4451192cd17748c568c38",
        "ad428638191f4f1cbb14a502212a4f91", 
        wv_service)
    ## 
    ## tweets BW
    wv_service = WordVectorsService(wv_rep.get("tweets.txt.usu.bw.kvs"))
    pred.predict_unlabeled_comments_and_save(
        "intertass-CR-test.xml",
        "b2d05dccbb6e490881df2d1d0da1601c",
        "e9d9a9a75d6741e9be0d7ce463ca0574", 
        wv_service)
    ##    
    ## tweets SW
    wv_service = WordVectorsService(wv_rep.get("tweets.txt.usu.sw.kvs"))
    pred.predict_unlabeled_comments_and_save(
        "intertass-CR-test.xml",
        "7007407a11104fe39212aa2db614b89e",
        "9212f907606a4d0e8e50bd8e449f21c3", 
        wv_service)
    ##  
    ## cardellino
    wv_service = WordVectorsService(wv_rep.get("SBW-vectors-300-min5.bin"))
    pred.predict_unlabeled_comments_and_save(
        "intertass-CR-test.xml",
        "c091629b547640828d350a4333def574",
        "d11f6e8914c14c8f9278a3cf961c5ba7", 
        wv_service)
    ##  
  