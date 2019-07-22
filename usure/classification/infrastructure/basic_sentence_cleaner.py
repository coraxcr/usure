from usure.classification.core import SentenceCleaner
from usure.preprocessing.cleaning import CleaningTask
from usure.preprocessing.infrastructure import EmoticonRep, StopwordsRep


class BasicSentenceCleaner(SentenceCleaner):

    def __init__(self, folderpath: str):
        self._cleaner = CleaningTask.create_basic(
            EmoticonRep(folderpath), StopwordsRep(folderpath))

    def clean(self, text: str) -> str:
        return self._cleaner.clean(text)
