import logging
import time 
import os
import math
import numpy as np
from pandas import DataFrame
import warnings
from multiprocessing import Pool, Value 
from ctypes import c_int

from usure.preprocessing.cleaning import CleaningTask
from usure.preprocessing.application.factories.usurecleaningtaskfactory import UsureCleaningTaskFactory 
from usure.preprocessing.infrastructure import CorpusDAO, TwitterCorpusDAO, FacebookCorpusDAO, TestCorpusDAO


class ETL:

    def __init__(self, cleaningtask:CleaningTask, corpus_dao:CorpusDAO):
        logging.basicConfig(level=logging.INFO)
        warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
        self._cleaningtask = cleaningtask
        self._corpus_dao = corpus_dao
        self._t = 0
        self.line_number = 0

    def _extract(self):
        df = self._corpus_dao.get_corpus_by_chunks()
        return df

    def _transform(self, reader) -> DataFrame:  
        processedcomments = []
        with Pool(processes=8) as p:
            counter = 0
            for chunk in reader:
                logging.info(f"Chunk: {counter} Starting time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
                chunk.dropna(inplace=True)
                commentslist = chunk.iterrows()
                processedcomments.extend(p.map(self._map_to_each_line, commentslist))
                counter += 1

        df = DataFrame(processedcomments)
        df.replace("", np.nan, inplace=True)
        df.dropna(inplace=True)
        return df

    def _load(self, df:DataFrame):
        self._corpus_dao.store_corpus(df)

    def _map_to_each_line(self,row):
        text = row[1][0]   
        try:
            result = self._cleaningtask.clean(text)
        except:
            print(f"AQUI=======> {text}linea:{self.line_number}")
            raise
        return result

    def _log_time(self, function, name):
        logging.info(f"Start {name} Starting time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
        self._t = time.process_time()
        result = function()
        elapsed_time = time.process_time() - self._t
        logging.info(f"End {name}: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")
        return result

    def do(self):
        data = self._log_time(self._extract, "EXTRACTING")
        data = self._log_time(lambda: self._transform(data), "TRANSFORMING")
        self._log_time(lambda: self._load(data), "LOADING")
        


if __name__ == "__main__":
    cleaningtaskfactory = UsureCleaningTaskFactory()
    cleaningtask = cleaningtaskfactory.create_twitter_process()
    corpusdao = TestCorpusDAO()
    etl = ETL(cleaningtask, corpusdao)
    etl.do()