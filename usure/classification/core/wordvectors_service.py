from  typing import Iterable
import numpy as np 
from .wordvectors import WordVectors
from usure.common import logging


class WordVectorsService:

    def __init__(self, wv:WordVectors):
        self._wv = wv

    @property
    def name(self) -> str:
        return self._wv.name

    @property
    def vector_size(self):
        return self._wv.vector_size

    def texts_to_padded_vectors(self, comment_max_length, texts:Iterable[str]):
        return np.array([self.text_to_padded_vectors(text, comment_max_length) for text in texts])

    def text_to_padded_vectors(self, text:str, comment_max_length):
        vectorized_text = self.text_to_vectors(text)
        vectorized_padded_text = np.zeros((comment_max_length, self.vector_size))
        for vector_index, vector in enumerate(vectorized_text):
            vectorized_padded_text[vector_index] = vector
        return vectorized_padded_text

    def texts_to_vectors(self, texts:Iterable[str]):
        return np.array([self.text_to_vectors(text) for text in texts])

    def text_to_vectors(self, text:str):
        return np.array([self._get_vector(token) for token in self._tokenize(text)])

    def _tokenize(self, text):
        return np.array(text.split(), dtype=object)

    def _get_vector(self, token):
        if token not in self._wv.wordvectors:
            logging.info(f"Token \"{token}\" not found in {self._wv.name}.")
            return np.zeros((1, self._wv.vector_size), dtype=float)
        else: 
            return self._wv.wordvectors[token]
