import pytest
from usure.config import config
from usure.classification.infrastructure import FileLabeledCommentsDao, BasicSentenceCleaner
config.set_to_test_mode()

cleaner = BasicSentenceCleaner(config.assets)

def can_instantiate_test():
    dao = FileLabeledCommentsDao(config.classification, cleaner)

def shuld_return_labeledcomments_test():
    dao = FileLabeledCommentsDao(config.classification, cleaner)
    comments = dao.get("test_0.xml")
    assert comments.count == 3

"""
def max_comments_len_labeledcomments_test(): #15 palabras intertass-CR-test.xml intertass-CR-train-tagged.xml
    dao = FileLabeledCommentsDao(config.classification, cleaner)
    comments = dao.get("intertass-CR-test.xml")
    max_val = len(max(comments.comments, key = lambda comment: len(comment.split())).split())
    assert max_val > 0
"""
