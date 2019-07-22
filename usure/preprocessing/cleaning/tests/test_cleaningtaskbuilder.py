import pytest
from usure.preprocessing.cleaning import (
    DiacriticCleaner, EmoticonCleaner, HashtagClener, CleanersBuilder)
from usure.preprocessing.infrastructure.tests.emoticonrep_stub import emoticon_stub_rep


def contains_three_cleaners_test(emoticon_stub_rep):
    builder = CleanersBuilder()
    cleaners = (builder
                .add_diacriticcleaning()
                .add_emoticoncleaning(emoticon_stub_rep)
                .add_hashtagcleaning()
                .build())
    assert len(cleaners) == 3


def contains_correct_cleaners_test(emoticon_stub_rep):
    builder = CleanersBuilder()
    cleaners = (builder
                .add_diacriticcleaning()
                .add_emoticoncleaning(emoticon_stub_rep)
                .add_hashtagcleaning()
                .build())
    assert isinstance(cleaners[0], DiacriticCleaner)
    assert isinstance(cleaners[1], EmoticonCleaner)
    assert isinstance(cleaners[2], HashtagClener)
