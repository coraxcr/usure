import pytest
from usure.preprocessing.infrastructure.emoticon_repository import EmoticonRepository
from usure.preprocessing.infrastructure.tests import config


repository = EmoticonRepository(config.assets)


def can_find_a_negative_emoticon_test():
    emoticons = repository.get_negative_emoticons()
    assert ":(" in emoticons


def can_find_a_positive_emoticon_test():
    emoticons = repository.get_positive_emoticons()
    assert ":)" in emoticons
