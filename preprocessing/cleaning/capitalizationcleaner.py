from usure.preprocessing.cleaning.cleaner import Cleaner


class CapitalizationCleaner(Cleaner):

    def clean(self, text:str):
        return text.lower()
