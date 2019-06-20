from usure.preprocessing.cleaning.cleaner import Cleaner
import re

class MentionCleaner(Cleaner):

    def __init__(self):
        self.__pattern = re.compile("((\s+@)|(^@))\w+")

    def clean(self, text):
        cleaned_text =  self.__pattern.sub("", text)
        return cleaned_text
