from usure.wordvectors.infrastructure import TrainingCorpusDAO


class TestTrainingCorpusDAO(TrainingCorpusDAO):
    
    def get_trainingcorpus(self):
        return self._get_trainingcorpus("test.usu")