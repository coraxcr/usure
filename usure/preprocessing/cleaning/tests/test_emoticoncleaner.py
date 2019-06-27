from usure.preprocessing.cleaning.emoticoncleaner import EmoticonCleaner
from usure.preprocessing.infrastructure import emoticon_stub_repository


def can_substitute_negative_emoticons_test(emoticon_stub_repository):
    cleaner = EmoticonCleaner(emoticon_stub_repository)
    text = "Hola mundo cruel :("
    result = cleaner.clean(text)
    assert result == "Hola mundo cruel negativeemoticon"

def can_substitute_positive_emoticons_test(emoticon_stub_repository):
    cleaner = EmoticonCleaner(emoticon_stub_repository)
    text = "Hola mundo cruel :)"
    result = cleaner.clean(text)
    assert result == "Hola mundo cruel positiveemoticon"


def can_substitute_positive_and_negative_emoticons_test(emoticon_stub_repository):
    cleaner = EmoticonCleaner(emoticon_stub_repository)
    text = "Hola mundo cruel :) :("
    result = cleaner.clean(text)
    assert result == "Hola mundo cruel positiveemoticon negativeemoticon"