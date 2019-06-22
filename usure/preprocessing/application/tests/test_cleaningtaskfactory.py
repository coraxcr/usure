import pytest
from usure.preprocessing.application.factories.usurecleaningtaskfactory import UsureCleaningTaskFactory
from usure.preprocessing.cleaning import (DiacriticCleaner, EmoticonCleaner, HashtagClener, CleaningTask)

def can_instantiate_factory_test():
    factory = UsureCleaningTaskFactory()
    cleaner = factory.create_basic_process()
    assert isinstance(cleaner, CleaningTask)