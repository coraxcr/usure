from typing import Iterable
import numpy as np
from sklearn.preprocessing import LabelEncoder
from .labeled_comments import LabeledComments
from .wordvectors_service import WordVectorsService


class ClassifierInput:

    def __init__(self, labeled_comments:LabeledComments, wv_service:WordVectorsService, categories=[]):
        """categories: only valid if labeled comments does not have labels."""
        self._labeled_comments = labeled_comments
        self._wv_service = wv_service
        self._categories = categories
        self._x_vectorized = np.array([])
        self._y_indexes = np.array([])
        self._x_vectorized_mean = np.array([])

    @property
    def embeddings_name(self):
        return self._wv_service.name

    @property
    def comment_max_length(self):
        return 20

    @property
    def vector_size(self):
        return self._wv_service.vector_size

    @property
    def labeled_comments(self):
        return self._labeled_comments

    @property 
    def categories(self):
        if not any(self._categories):
            label_encoder = LabelEncoder()
            label_encoder.fit_transform(self._labeled_comments.labels)
            self._categories = label_encoder.classes_
        return self._categories

    @property
    def x_vectorized(self):
        if not self._x_vectorized.any():
            no_texts = len(self._labeled_comments.comments)
            padded_texts = self._wv_service.texts_to_padded_vectors(self.comment_max_length,
                self._labeled_comments.comments)
            self._x_vectorized = padded_texts
        return self._x_vectorized
    
    @property 
    def x_vectorized_mean(self):
        if not self._x_vectorized_mean.any():
            self._x_vectorized_mean = np.array([np.mean(np.array(comment, dtype=float), axis=0) for comment in self.x_vectorized])
        return np.array(self._x_vectorized_mean)
    
    @property 
    def y_indexes(self):
        if not self._y_indexes.any():
            label_encoder = LabelEncoder()
            self._y_indexes = label_encoder.fit_transform(self._labeled_comments.labels)
        return np.array(self._y_indexes, dtype=int)