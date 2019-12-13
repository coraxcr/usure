from typing import List
from functools import reduce
from usure.preprocessing.cleaning import Cleaner, CleanersBuilder
from usure.preprocessing.infrastructure import EmoticonRep, StopwordsRep


class CleaningTask:

    def __init__(self, cleaners: List[Cleaner]):
        assert cleaners, "There are no cleaners."
        self.__cleaners = cleaners

    def clean(self, text: str) -> str:
        assert text, "There is no text."
        cleaned_text = reduce(lambda text, cleaner: cleaner.clean(
            text), self.__cleaners, text)
        return cleaned_text

    @classmethod
    def create_basic(cls, emoticonrep: EmoticonRep, stopwordsrep: StopwordsRep):
        cleaners = (CleanersBuilder()
                    .add_htmlcleaning()
                    .add_urlcleaning()
                    .add_escapecleaner()
                    .add_mentioncleaning()
                    .add_hashtagcleaning()
                    .add_emoticoncleaning(emoticonrep)
                    .add_captalizationcleaning()
                    .add_wordlengtheningcleaning()
                    .add_puntuationcleaning()
                    #.add_stopwordscleaning(stopwordsrep)
                    .add_diacriticcleaning()
                    .add_numericcleaner()
                    .add_encodingcleaning()
                    .build())
        return cls(cleaners)

    @classmethod
    def create_twitter(cls, emoticonrep: EmoticonRep, stopwordsrep: StopwordsRep):
        cleaners = (CleanersBuilder()
                    .add_twittercorpuscleaner()
                    .add_htmlcleaning()
                    .add_urlcleaning()
                    .add_escapecleaner()
                    .add_mentioncleaning()
                    .add_hashtagcleaning()
                    .add_emoticoncleaning(emoticonrep)
                    .add_captalizationcleaning()
                    .add_wordlengtheningcleaning()
                    .add_puntuationcleaning()
                    #.add_stopwordscleaning(stopwordsrep)
                    .add_diacriticcleaning()
                    .add_numericcleaner()
                    .add_encodingcleaning()
                    .build())
        return cls(cleaners)
