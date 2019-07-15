import os
from usure.preprocessing.infrastructure import FileCorpusRepository
from usure.preprocessing.core import Corpus
import pytest

testpath = os.path.join(os.path.dirname(__file__), "assets/corpora")
repository = FileCorpusRepository(testpath)
corpusname = "test.txt"

def can_get_a_corpus_test():
    corpus = repository.get(corpusname)

def are_there_sentences_in_a_corpus_test():
    corpus = repository.get(corpusname)
    sentences = list(corpus)
    assert len(sentences) > 0

def can_get_all_corpus_test():
    corpora = repository.get_all()

def can_get_all_sentences_in_all_corpus_test():
    corpora = repository.get_all()
    for corpus in corpora:
        sentences = list(corpus)
        assert len(sentences) > 0
        
def must_add_test():
    get_sentences = lambda: ["hola mundo", "hola mundo"]
    corpus = Corpus("test.usu", get_sentences)
    repository.save(corpus)