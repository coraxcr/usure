from usure.wordvectors.infrastructure import TrainingCorpusDAO


class TwitterTrainingCorpusDAO(TrainingCorpusDAO):
    
    def get_trainingcorpus(self):
        return self._get_trainingcorpus("twitter.usu")