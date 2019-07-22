import pytest
from usure.preprocessing.infrastructure import StopwordsRep


@pytest.fixture
def stopwords_stub_rep(mocker):
    rep = StopwordsRep("test")
    mocker.patch.object(rep, 'get_spanish_stopwords', return_value={
                        "el", "había", "habia", "estado", "en", "la"})
    return rep
