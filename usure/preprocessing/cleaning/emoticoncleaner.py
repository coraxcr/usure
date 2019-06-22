from usure.preprocessing.cleaning.cleaner import Cleaner
from gensim import utils


class EmoticonCleaner(Cleaner):

    def __init__(self, emoticonrepository):
        self.__emoticonrepository = emoticonrepository

    def clean(self, text: str) -> str:
        tokens = text.split(' ') 
        cleanedtokens = map(self.__substitute_by_placeholder, tokens)
        return ' '.join(cleanedtokens)

    
    def __substitute_by_placeholder(self, token):
        positiveemoticons = self.__emoticonrepository.get_positive_emoticons()
        negativeemoticons = self.__emoticonrepository.get_negative_emoticons()
        if token in positiveemoticons:
            return "positive_emoticon"
        elif token in negativeemoticons:
            return "negative_emoticon"
        else: 
            return token

#from nltk.tokenize import word_tokenize
#tokens = word_tokenize(input_str)
#stop_words = set(stopwords.words(‘english’))
#from nltk.corpus import stopwords