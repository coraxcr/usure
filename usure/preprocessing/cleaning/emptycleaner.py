from usure.preprocessing.cleaning import Cleaner

class EmptyCleaner(Cleaner):

    def clean(self, text:str)->str:
        if text is None:
            return ""
        return text