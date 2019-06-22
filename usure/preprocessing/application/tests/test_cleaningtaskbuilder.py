import pytest
from usure.preprocessing.application.factories.cleaningtaskbuilder import CleaningTaskBuilder
from usure.preprocessing.cleaning import (DiacriticCleaner, EmoticonCleaner, HashtagClener)

def contains_three_cleaners_test():
    builder = CleaningTaskBuilder()
    cleaners = (builder
        .add_diacriticcleaning()
        .add_emoticoncleaning()
        .add_hashtagcleaning()
        .build())
    assert len(cleaners) == 3


def contains_correct_cleaners_test():
    builder = CleaningTaskBuilder()
    cleaners = (builder
        .add_diacriticcleaning()
        .add_emoticoncleaning()
        .add_hashtagcleaning()
        .build())
    assert isinstance(cleaners[0], DiacriticCleaner)
    assert isinstance(cleaners[1], EmoticonCleaner)
    assert isinstance(cleaners[2], HashtagClener)
