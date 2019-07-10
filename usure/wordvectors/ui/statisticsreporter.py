import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from wordcloud import WordCloud
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors, Vocab
from typing import Dict, List

from usure.wordvectors.infrastructure import Word2VecDAO


class StatisticsReporter:

    def start(self):
        self.extract_models()

    def extract_models(self):
        w2v_dao = Word2VecDAO()
        models = w2v_dao.get_models()
        for w2v in  models:
            sorted_vocabulary = self.order_by_frequence(w2v.wv.vocab)
            #self.plot_histogram(sorted_vocabulary)
            ##vocabulary = np.array(sorted_vocabulary, dtype=object)
            ##words = vocabulary[:, 0]
            ##frequencies =  vocabulary[:, 1]
            items = w2v.wv.vocab.items()
            self.plot_wordcloud({ k:v.count for k,v in items})
            break
        
    def order_by_frequence(self, vocab:Dict[str, Vocab]):
        vocab_items = vocab.items()
        sorted_vocabulary = sorted(([k,v.count] for k,v in vocab_items), key=lambda item: item[1], reverse=True)
        return sorted_vocabulary

    def plot_histogram(self, sorted_vocabulary): #tipo
        numb_top_words = 75
        np_sorted_vocabulary = np.array(sorted_vocabulary, dtype=object)
        x_labels = np_sorted_vocabulary[:numb_top_words, 0]
        y_frequencies = np_sorted_vocabulary[:numb_top_words, 1]
        x = np.arange(numb_top_words)
        plt.figure(figsize=(12,12))
        plt.bar(x, y_frequencies, align='center', alpha=0.5)
        plt.plot(x, y_frequencies, color='r', linestyle='--',linewidth=2,alpha=0.5)
        plt.xticks(x, x_labels, rotation='vertical')
        plt.ylabel('Frecuencia')
        plt.xlabel(f'{numb_top_words} palabras mas comunes')
        plt.show()

    def plot_wordcloud(self, words):
        wordcloud = WordCloud(width=1600, height=800, max_font_size=200)
        wordcloud.generate_from_frequencies(words)
        plt.figure(figsize=(12,10))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    st =  StatisticsReporter()
    st.start()
