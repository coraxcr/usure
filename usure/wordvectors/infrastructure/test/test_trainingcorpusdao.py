from usure.wordvectors.infrastructure import TestTrainingCorpusDAO

def no_errors_extracting_trainingcorpus_test():
    dao = TestTrainingCorpusDAO()
    sentences = dao.get_trainingcorpus()