from typing import List
from usure.preprocessing.cleaning import (
    CapitalizationCleaner,
    CharacterEncodingCleaner,
    Cleaner,
    DiacriticCleaner,
    EmoticonCleaner,
    HashtagClener,
    HtmlCleaner,
    LemmatizationCleaner,
    MentionCleaner,
    PuntuationCleaner,
    StopWordsCleaner,
    UrlCleaner,
    WordLengtheningCleaner,
    TwitterCorpusCleaner,
    NumericCleaner,
    EscapeCleaner
)
from usure.preprocessing.infrastructure import EmoticonRep, StopwordsRep


class CleanersBuilder:

    def __init__(self):
        self._cleaners = []

    def _add_cleaner(self, cleaner: Cleaner):
        self._cleaners.append(cleaner)

    def build(self) -> List[Cleaner]:
        return self._cleaners

    def add_captalizationcleaning(self):
        cleaner = CapitalizationCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_encodingcleaning(self):
        cleaner = CharacterEncodingCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_diacriticcleaning(self):
        cleaner = DiacriticCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_emoticoncleaning(self, repository: EmoticonRep):
        cleaner = EmoticonCleaner(repository)
        self._add_cleaner(cleaner)
        return self

    def add_hashtagcleaning(self):
        cleaner = HashtagClener()
        self._add_cleaner(cleaner)
        return self

    def add_htmlcleaning(self):
        cleaner = HtmlCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_lemmatizationcleaning(self):
        cleaner = LemmatizationCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_mentioncleaning(self):
        cleaner = MentionCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_puntuationcleaning(self):
        cleaner = PuntuationCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_stopwordscleaning(self, repository: StopwordsRep):
        cleaner = StopWordsCleaner(repository)
        self._add_cleaner(cleaner)
        return self

    def add_urlcleaning(self):
        cleaner = UrlCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_wordlengtheningcleaning(self):
        cleaner = WordLengtheningCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_twittercorpuscleaner(self):
        cleaner = TwitterCorpusCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_numericcleaner(self):
        cleaner = NumericCleaner()
        self._add_cleaner(cleaner)
        return self

    def add_escapecleaner(self):
        cleaner = EscapeCleaner()
        self._add_cleaner(cleaner)
        return self
