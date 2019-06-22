from usure.preprocessing.cleaning.urlcleaner import UrlCleaner


def remove_all_urls_test():
    text = "visit our page at www.google.com or http://fb.com"
    cleaned_text = "visit our page at  or "
    cleaner = UrlCleaner()
    result = cleaner.clean(text)
    assert result == cleaned_text