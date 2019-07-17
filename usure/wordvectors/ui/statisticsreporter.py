import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE
from wordcloud import WordCloud
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors, Vocab
from typing import Dict, List
from usure.wordvectors.infrastructure import Word2VecDAO, KeyedVectorsDAO


class StatisticsReporter:

    def __init__(self, keyed_vectors: KeyedVectors):
        self._keyed_vectors = keyed_vectors
        self._freq_dict = {word: vocab.count for word,
                           vocab in self._keyed_vectors.vocab.items()}

    def plot_wordcloud(self, max_words=250):
        wordcloud = WordCloud(width=1600, height=800,
                              max_font_size=200, max_words=max_words)
        wordcloud.generate_from_frequencies(self._freq_dict)
        plt.figure(figsize=(12, 10))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def plot_histogram(self, numb_top_words=100):
        sorted_vocabulary = self._order_by_frequence(self._freq_dict)
        np_sorted_vocabulary = np.array(sorted_vocabulary, dtype=object)
        x_labels = np_sorted_vocabulary[:numb_top_words, 0]
        y_frequencies = np_sorted_vocabulary[:numb_top_words, 1]
        x = np.arange(numb_top_words)
        plt.figure(figsize=(13, 12))
        plt.bar(x, y_frequencies, align='center', alpha=0.5)
        plt.plot(x, y_frequencies, color='r',
                 linestyle='--', linewidth=2, alpha=0.5)
        plt.xticks(x, x_labels, rotation='vertical')
        plt.ylabel('Frecuencia')
        plt.xlabel(f'{numb_top_words} palabras mas comunes')
        plt.show()

    def plot_scatter(self, numb_words=1000, num_dim=2):
        vocabulary, vectors = self._get_vocabulary_and_vectors(
            self._keyed_vectors, numb_words)
        reduced_vectors = self._reduce_vectors_dimention(vectors, num_dim)
        if num_dim == 2:
            self._plot_scatter_2d(vocabulary, reduced_vectors)
        elif num_dim == 3:
            self._plot_scatter_3d(vocabulary, reduced_vectors)

    def _plot_scatter_2d(self, vocabulary, reduced_vectors):
        fig, ax = plt.subplots()
        xs = reduced_vectors[:, 0]
        ys = reduced_vectors[:, 1]
        ax.scatter(xs, ys, marker='o', s=10)
        plt.axis('off')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        # ax.legend(["Palabras"])
        for vector, word in zip(reduced_vectors, vocabulary):
            ax.text(x=vector[0], y=vector[1], s=word, fontsize=6)
        plt.show()

    def _plot_scatter_3d(self, vocabulary, reduced_vectors):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        xs = reduced_vectors[:, 0]
        ys = reduced_vectors[:, 1]
        zs = reduced_vectors[:, 2]
        ax.scatter(xs, ys, zs, marker='o', s=10)
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.set_zlabel('Eje Z')
        ax.legend(["Palabras"])
        for vector, word in zip(reduced_vectors, vocabulary):
            ax.text(x=vector[0], y=vector[1], z=vector[2], s=word, fontsize=6)
        plt.show()

    def _order_by_frequence(self, vocab: Dict[str, int]):
        vocab_items = vocab.items()
        sorted_vocabulary = sorted(
            ([k, v] for k, v in vocab_items), key=lambda item: item[1], reverse=True)
        return sorted_vocabulary

    def _get_vocabulary_and_vectors(self, keyed_vectors: KeyedVectors, numb_words: int):
        vocabulary = np.array(
            [word for word, vocab in keyed_vectors.vocab.items()][:numb_words], dtype=object)
        vectors = np.array([keyed_vectors.get_vector(word)
                            for word in vocabulary])
        return vocabulary, vectors

    def _reduce_vectors_dimention(self, vectors, num_dim=2):
        tsne = TSNE(n_components=num_dim, random_state=0)
        reduced_vectors = tsne.fit_transform(vectors)
        return np.array(reduced_vectors)


if __name__ == "__main__":
    kvs_dao = KeyedVectorsDAO()
    facebook2013 = kvs_dao.get_model("sbw_vectors.bin")
    st = StatisticsReporter(facebook2013.wv)
    st.plot_wordcloud(max_words=250)
    st.plot_histogram(numb_top_words=60)
    st.plot_scatter(numb_words=1000, num_dim=2)
