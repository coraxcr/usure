from usure.wordvectors.infrastructure import TrainingCorpusDAO


class FbTrainingCorpusDAO(TrainingCorpusDAO):
    
    def get_trainingcorpus(self):
        return self._get_trainingcorpus("CorpusFBCR2013.usu")
