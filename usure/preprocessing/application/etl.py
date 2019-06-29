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
from usure.preprocessing.application.factories import UsureCleaningTaskFactory, CorpusDAOFactory
from usure.preprocessing.infrastructure import CorpusDAO


class ETL:

    def __init__(self, cleaningtask:CleaningTask, corpusdao:CorpusDAO):
        logging.basicConfig(level=logging.INFO)
        warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
        self._cleaningtask = cleaningtask
        self._corpusdao = corpusdao

    @property
    def cleaningtask(self):
        return self._cleaningtask
    
    @cleaningtask.setter
    def cleaningtask(self, value):
        assert isinstance(value, CleaningTask), "Not a Cleaning task"
        self._cleaningtask = value

    @property
    def corpusdao(self):
        return self._cleaningtask
    
    @corpusdao.setter
    def corpusdao(self, value):
        assert isinstance(value, CorpusDAO), "Not a CorpusDAO task"
        self._cleaningtask = value

    def _extract(self):
        df = self._corpusdao.get_corpus_by_chunks()
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
        self._corpusdao.store_corpus(df)

    def _map_to_each_line(self,row):
        text = row[1][0]   
        try:
            result = self._cleaningtask.clean(text)
        except:
            print(f"Error text of the line: \"{text}\"")
            raise
        return result

    def _log_time(self, task, name):
        logging.info(f"Start {name} Starting time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
        start_process_time = time.process_time()
        result = task()
        elapsed_time = time.process_time() - start_process_time
        logging.info(f"End {name}: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")
        return result

    def do(self):
        data = self._log_time(self._extract, "EXTRACTING")
        data = self._log_time(lambda: self._transform(data), "TRANSFORMING")
        self._log_time(lambda: self._load(data), "LOADING")
        


if __name__ == "__main__":

    cleaningtaskfactory = UsureCleaningTaskFactory()
    corpusdaofactory = CorpusDAOFactory()

    cleaningtask = cleaningtaskfactory.create_basic_process()
    corpusdao = corpusdaofactory.create_facebook()

    etl = ETL(cleaningtask, corpusdao)

    etl.do() 