import pytest
from usure.preprocessing.infrastructure import StopwordsRepository


@pytest.fixture
def stopwords_stub_repository(mocker):
    rep = StopwordsRepository("test")
    mocker.patch.object(rep, 'get_spanish_stopwords', return_value={
                        "el", "había", "habia", "estado", "en", "la"})
    return rep
