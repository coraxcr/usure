import pytest
from usure.preprocessing.application.factories.cleaningprocessfactory import CleaningFactory
from usure.preprocessing.cleaning import (DiacriticCleaner, EmoticonCleaner, HashtagClener)

def can_instantiate_factory_test():
    factory = CleaningFactory()
    cleaner = factory.create_basic_process()
    assert isinstance(cleaner, CleaningFactory)