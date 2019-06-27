from usure.preprocessing.cleaning.cleaner import Cleaner
import re

class PuntuationCleaner(Cleaner):


    def __init__(self):
        spanish_punctuation =  r"""!¡"#$%&'()*+,-./:;<=>¿?@[\]^_`{|}~¨´§«»¶\\"""
        self.__pattern = re.compile(f"[{spanish_punctuation}]")

    def clean(self, text:str) -> str:
        cleaned_text = self.__pattern.sub(" ", text)
        return cleaned_text
