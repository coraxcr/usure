import pandas as pd
from pandas import DataFrame
import logging
import time 
import os
import math
from usure.preprocessing.cleaning import CleaningTask
from usure.preprocessing.application.factories.usurecleaningtaskfactory import UsureCleaningTaskFactory 
from usure.preprocessing.infrastructure import CorpusDAO
import warnings

class ETL:

    def __init__(self):
        cleaningtaskfactory = UsureCleaningTaskFactory()
        logging.basicConfig(level=logging.INFO)
        warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
        self._cleaningtask = cleaningtaskfactory.create_basic_process()
        self._corpus_dao = CorpusDAO()
        self.line_number = 0

    def _extract(self):
        df = self._corpus_dao.get_facebookcorpus()
        return df

    def _transform(self, df:DataFrame) -> DataFrame:
        return df.applymap(self._map_to_each_line)

    def _load(self, df:DataFrame):
        self._corpus_dao.store_facebookcorpus(df)

    def _map_to_each_line(self, text :str):
        if math.fmod(self.line_number, 500000) == 0:
            logging.info(f"Processed lines: {self.line_number}")  
        self.line_number += 1
        return self._cleaningtask.clean(text)

    def _log_time(self, function, name):
        logging.info(f"Starting {name}")
        t = time.process_time()
        result = function()
        elapsed_time = time.process_time() - t
        logging.info(f"End {name}: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")
        return result

    def do(self):
        data = self._log_time(self._extract, "EXTRACT")
        data = self._log_time(lambda: self._transform(data), "TRANSFORM")
        self._log_time(lambda: self._load(data), "LOAD")
        


if __name__ == "__main__":
    etl = ETL()
    etl.do()