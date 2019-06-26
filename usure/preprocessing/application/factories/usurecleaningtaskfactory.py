from typing import List
from usure.preprocessing.cleaning import (
    CleaningTask,
    CleaningTaskFactory,
)
from .cleaningtaskbuilder import CleaningTaskBuilder


class UsureCleaningTaskFactory(CleaningTaskFactory):

    def __init__(self):
        self._builder = CleaningTaskBuilder()

    def create_basic_process(self) -> CleaningTask:
        cleaners = (self._builder
        #.add_emptycleaner()
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
        return CleaningTask(cleaners)

    def create_twitter_process(self) -> CleaningTask:
        cleaners = (self._builder
        #.add_emptycleaner()
        .add_twittercorpuscleaner()
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
        return CleaningTask(cleaners)

        
        
        
        
