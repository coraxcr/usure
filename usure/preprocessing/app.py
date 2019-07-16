import logging
import time 
import os
from multiprocessing import Pool, Value, cpu_count 
from typing import Dict, Iterator, Callable
import itertools
from usure.preprocessing.cleaning import CleaningTask
from usure.preprocessing.core import Corpus, CorpusRepository
from usure.preprocessing import config
from usure.preprocessing.infrastructure import FileCorpusRepository
import usure.common.logging as usurelogging


usurelogging.config(config.log_path)

class App:

    def __init__(self, raw_corpus_rep:CorpusRepository,
        pre_corpus_rep:CorpusRepository,
        get_cleaningtask:Callable[[str], CleaningTask]):
        self._get_cleaningtask = get_cleaningtask
        self._raw_corpus_rep = raw_corpus_rep
        self._pre_corpus_rep = pre_corpus_rep

    def _extract(self):
        corpora = self._raw_corpus_rep.get_all()
        return corpora

    @usurelogging.logtime
    def _transform(self, corpus:Corpus) -> Corpus:  
        processed_sentences = []
        usurelogging.info_time(f"Corpus: {corpus.name}")
        with Pool(processes=cpu_count()) as pool:
            chunk_size = 400000
            chunk_numb = 0
            chunks = self._chunk(corpus, chunk_size)
            for chunk in chunks:
                sentences = pool.map(self._map_to_each_line, chunk)
                sentences = [sentence for sentence in sentences if sentence]
                processed_sentences.extend(sentences)
                chunk_numb += 1
                usurelogging.info_time(f"Processed: {chunk_size * chunk_numb}")
        return processed_sentences

    def _chunk(self, corpus:Corpus, chunk_size):
        chunk = []
        count  = 0
        for sentence in corpus:
            count += 1
            chunk.append((corpus.name, sentence))
            if count % chunk_size == 0:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

    def _map_to_each_line(self,chunk): 
        corpus_name, text = chunk
        try:
            result = self._get_cleaningtask(corpus_name).clean(text)
        except:
            print(f"Error text of the line: \"{text}\"")
            raise
        return result

    def do(self):
        corpora = self._extract()
        for corpus in corpora:
            sentences = self._transform(corpus)
            prepocessed_corpus = Corpus(f"{corpus.name}.usu", lambda: sentences)
            self._pre_corpus_rep.save(prepocessed_corpus)
        

if __name__ == "__main__":
    raw_corpus_rep = FileCorpusRepository(config.raw_corpora_folder_path)
    pre_corpus_rep = FileCorpusRepository(config.preprocessed_corpora_folder_path)
    
    basic_cleaning_task = CleaningTask.create_basic()
    twiter_claning_task = CleaningTask.create_twitter()

    def get_cleaningtask(name:str):
        if name == "tweets.txt":
            return twiter_claning_task
        else:
            return basic_cleaning_task
    
    etl = App(raw_corpus_rep, pre_corpus_rep, get_cleaningtask)
    etl.do()