from usure.preprocessing.cleaning.htmlcleaner import HtmlCleaner


to_clean = '<a href="#example">Example headline</a><div>hola</div>E tu vivrai nel terrore - L&#x27;aldil&#xE0; (1981) &amp;'
correctly_cleaning = 'Example headlineholaE tu vivrai nel terrore - L\'aldilà (1981) &'


def can_replace_all_htmlentities_test():
    cleaner = HtmlCleaner()
    cleaned_text = cleaner.clean(to_clean)
    assert cleaned_text == correctly_cleaning


def is_cleaned_result_disting_from_toclean_test():
    cleaner = HtmlCleaner()
    cleaned_text = cleaner.clean(to_clean)
    assert cleaned_text != to_clean
