from usure.preprocessing.cleaning.cleaner import Cleaner
from nltk.tokenize import word_tokenize

class CharacterEncodingCleaner(Cleaner):

    def clean(self, text:str) -> str:
        tokens = word_tokenize(text, language="spanish")
        tokens = [token for token in tokens if token.isascii()] #.encode("ascii", "ignore") 
        return " ".join(tokens)