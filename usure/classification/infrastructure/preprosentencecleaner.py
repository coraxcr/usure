from usure.classification.core import SentenceCleaner
from usure.preprocessing.cleaning import CleaningTask

class PreproSentenceCleaner(SentenceCleaner):

    def __init__(self):
        self._cleaner = CleaningTask.create_basic()

    def clean(text:str) -> str:
        return self._cleaner.clean(text)

