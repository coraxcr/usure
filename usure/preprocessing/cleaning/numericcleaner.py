import re
from .cleaner import Cleaner
from nltk.tokenize import sent_tokenize, word_tokenize

class NumericCleaner(Cleaner):

    def clean(self, text:str)->str:
        tokens = word_tokenize(text)
        result = [token for token in tokens if not token.isnumeric()]
        result = " ".join(result)
        return result
