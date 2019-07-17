from usure.preprocessing.cleaning.diacriticcleaner import DiacriticCleaner


to_clean = 'Šéf chomutovských komunistů dostal poštou bílý prášek, Qué oración más simpática! España Yigüirro'
correctly_cleaning = 'Sef chomutovskych komunistu dostal postou bily prasek, Que oracion mas simpatica! Espana Yiguirro'


def can_remove_all_diacritics_test():
    cleaner = DiacriticCleaner()
    cleaned_text = cleaner.clean(to_clean)
    assert cleaned_text == correctly_cleaning


def is_cleaned_result_disting_from_toclean_test():
    cleaner = DiacriticCleaner()
    cleaned_text = cleaner.clean(to_clean)
    assert cleaned_text != to_clean
