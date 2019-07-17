from usure.preprocessing.cleaning.cleaner import Cleaner
import re
# nltk.tokenize.casual.reduce_lengthening(text)


class WordLengtheningCleaner(Cleaner):

    def __init__(self):
        self.__pattern_letter = re.compile(r"(.)\1{2,}")  # more than 2 lleters
        self.__pattern_sillable = re.compile(
            r"(\w{2})\1{2,}")  # more than 2 syllable

    def clean(self, text: str) -> str:
        cleaned_text = self.__pattern_sillable.sub(r"\1\1", text)
        cleaned_text = self.__pattern_letter.sub(r"\1\1", cleaned_text)
        return cleaned_text
