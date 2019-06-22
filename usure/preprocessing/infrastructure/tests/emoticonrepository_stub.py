import pytest
from usure.preprocessing.infrastructure.emoticon_repository import EmoticonRepository

@pytest.fixture
def emoticon_stub_repository(mocker):
    rep = EmoticonRepository()
    mocker.patch.object(rep, 'get_negative_emoticons', return_value = {":(", ":-("})
    mocker.patch.object(rep, 'get_positive_emoticons', return_value = {":)", ":-)"})
    return rep