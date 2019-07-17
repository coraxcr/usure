from usure.preprocessing.cleaning.stopwordscleaner import StopWordsCleaner
from usure.preprocessing.infrastructure.tests.stopswordsrepository_stub import stopwords_stub_repository 


def can_remove_spanish_stopwords_test(stopwords_stub_repository):
    text = "el carro había habia estado en la casa"
    cleaned_text = "carro casa"
    cleaner = StopWordsCleaner(stopwords_stub_repository)
    result = cleaner.clean(text)
    assert cleaned_text == result

'''
def not_allowed_not_alphanumericwords_test():
    text = "Hola ca2df 4ndr32"
    cleaned_text = "Hola"
    cleaner = StopWordsCleaner(StopwordsRepository())
    result = cleaner.clean(text)
    assert cleaned_text == result
'''