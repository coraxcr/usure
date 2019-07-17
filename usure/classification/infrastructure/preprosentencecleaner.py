from usure.classification.core import SentenceCleaner
from usure.preprocessing.cleaning import CleaningTask
from usure.preprocessing.infrastructure import EmoticonRepository, StopwordsRepository


class PreproSentenceCleaner(SentenceCleaner):

    def __init__(self, folderpath: str):
        self._cleaner = CleaningTask.create_basic(
            EmoticonRepository(folderpath), StopwordsRepository(folderpath))

    def clean(text: str) -> str:
        return self._cleaner.clean(text)
