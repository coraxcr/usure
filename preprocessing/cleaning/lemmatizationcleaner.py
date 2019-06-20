from usure.preprocessing.cleaning.cleaner import Cleaner
import spacy
import functools


class LemmatizationCleaner(Cleaner):


    def __init__(self):
        self.__sp = spacy.load('es_core_news_sm')

    def clean(self, text: str) -> str:
        procesed_text = self.__sp(text)
        result =  functools.reduce(lambda cumu, token: cumu+" "+token.lemma_, procesed_text, "")
        return result
