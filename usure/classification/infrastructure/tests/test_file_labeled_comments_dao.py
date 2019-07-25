import pytest
from usure.config import config
from usure.classification.infrastructure import FileLabeledCommentsDao 
config.set_to_test_mode()


def can_instantiate_test():
    dao = FileLabeledCommentsDao(config.classification)

def shuld_return_labeledcomments_test():
    dao = FileLabeledCommentsDao(config.classification)
    comments = dao.get("test_0.xml")
    assert comments.count == 3



