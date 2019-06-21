from typing import List
from usure.preprocessing.cleaning import (
    CleaningProcess,
    CleaningProcessFactory,
)
from .cleaningprocessbuilder import CleaningProcessBuilder



class CleaningFactory(CleaningProcessFactory):

    def __init__(self):
        self._builder = CleaningProcessBuilder()

    def create_basic_process(self) -> CleaningProcess:
        cleaners = (self._builder
        .add_htmlcleaning()
        .add_urlcleaning()
        .add_mentioncleaning()
        .add_hashtagcleaning()
        .add_emoticoncleaning()
        .add_captalizationcleaning()
        .add_wordlengtheningcleaning()
        .add_stopwordscleaning()
        .add_diacriticcleaning()
        .add_puntuationcleaning()
        .add_encodingcleaning()
        .build())
        return CleaningProcess(cleaners)

        
        
        
        
