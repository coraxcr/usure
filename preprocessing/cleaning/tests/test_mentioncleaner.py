from usure.preprocessing.cleaning.mentioncleaner import MentionCleaner


def can_rid_mentions_off_test():
    text = "@maria hola @juan y @maria cristian@hotmal.com"
    cleaned_text = " hola y cristian@hotmal.com"
    cleaner = MentionCleaner()
    result = cleaner.clean(text)
    assert result == cleaned_text