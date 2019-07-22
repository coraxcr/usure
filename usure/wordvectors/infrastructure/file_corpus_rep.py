from typing import Iterable, Iterator
from usure.wordvectors.core import Corpus
from usure.preprocessing.infrastructure import FileCorpusRep as PreprocessingFileCorpusRep
from usure.preprocessing.core import Corpus as PreprocessingCorpus


class FileCorpusRep:

    def __init__(self, folderpath: str):
        self.repository = PreprocessingFileCorpusRep(folderpath)

    def get(self, name: str) -> Corpus:
        precorpus = self.repository.get(name)
        corpus = self.mapcorpus(precorpus)
        return corpus

    def get_all(self) -> Iterable[Corpus]:
        precorpora = self.repository.get_all()
        return(self.mapcorpus(corpus) for corpus in precorpora)

    def mapcorpus(self, precorpus: PreprocessingCorpus) -> Corpus:

        def tokenize(sentences: Iterator[str]) -> Iterator[Iterator[str]]:
            return (sentence.split() for sentence in sentences)

        corpus = Corpus(precorpus.name, lambda: tokenize(precorpus.__iter__()))

        return corpus
