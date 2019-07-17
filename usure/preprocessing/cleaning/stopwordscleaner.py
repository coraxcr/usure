from usure.preprocessing.cleaning.cleaner import Cleaner
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim import utils


class StopWordsCleaner(Cleaner):

    def __init__(self, stopwords_repository):
        self.__stopwords = stopwords_repository.get_spanish_stopwords()

    def clean(self, text: str) -> str:
        tokens = word_tokenize(text)
        result = [token for token in tokens if self.is_a_valid_word(token)]
        result = " ".join(result)
        return result

    def is_a_valid_word(self, token: str):
        valid = token not in self.__stopwords
        #valid = token.isalpha() and valid
        return valid
