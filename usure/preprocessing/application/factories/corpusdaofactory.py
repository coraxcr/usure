from usure.preprocessing.infrastructure import FacebookCorpusDAO, TwitterCorpusDAO, TestCorpusDAO


class CorpusDAOFactory:

    def create_facebook(self):
        return FacebookCorpusDAO()

    def create_twitter(self):
        return TwitterCorpusDAO()

    def create_test(self):   
        return TestCorpusDAO()