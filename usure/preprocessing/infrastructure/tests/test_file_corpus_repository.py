import os
import pytest
from usure.preprocessing.infrastructure import FileCorpusRepository
from usure.preprocessing.core import Corpus
from usure.config import config

config.set_to_test_mode()

repository = FileCorpusRepository(config.unpreprocessed)
corpusname = "test_1.txt"


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
    def get_sentences(): return ["hola mundo", "hola mundo"]
    corpus = Corpus("test.usu", get_sentences)
    repository.save(corpus)
