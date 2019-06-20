from usure.preprocessing.cleaning.cleaner import Cleaner
from gensim import utils


class DiacriticCleaner(Cleaner):

    def clean(self, text: str) -> str:
        return utils.deaccent(text)
