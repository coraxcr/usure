from usure.preprocessing.cleaning.capitalizationcleaner import CapitalizationCleaner


def can_lowercase_text_test():
    text = "HOLA MunDo"
    cleaned_text = "hola mundo"
    cleaner = CapitalizationCleaner()
    result = cleaner.clean(text)
    assert result == cleaned_text