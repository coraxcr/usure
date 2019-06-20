from usure.preprocessing.cleaning.cleaner import Cleaner
import re 

class HashtagClener(Cleaner):

    def __init__(self):
        self.__pattern = re.compile("\s*#\w+")

    def clean(self, text):
        text = self.__pattern.sub("", text)
        return text