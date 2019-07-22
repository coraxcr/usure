import pytest
from usure.preprocessing.infrastructure import EmoticonRep


@pytest.fixture
def emoticon_stub_rep(mocker):
    rep = EmoticonRep("test")
    mocker.patch.object(rep, 'get_negative_emoticons',
                        return_value={":(", ":-("})
    mocker.patch.object(rep, 'get_positive_emoticons',
                        return_value={":)", ":-)"})
    return rep
