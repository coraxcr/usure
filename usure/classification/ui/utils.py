import os
import matplotlib.pyplot as plt
from matplotlib import markers 
import pandas as pd
from usure.classification.core import MetricsReporter


def plot_learning_curves(train_metrics:MetricsReporter, val_metrics:MetricsReporter):
    f, ax = plt.subplots(1, 2, figsize = (16, 7))
    epochs = range(1, len(train_metrics.accuracies) + 1)
    plt.sca(ax[0])
    plt.plot(epochs, train_metrics.accuracies, 'go-', label='Training')
    plt.plot(epochs, val_metrics.accuracies, 'ro-', label='Validation')
    plt.title('ACCURACY')
    plt.legend()
    plt.sca(ax[1])
    plt.plot(epochs, train_metrics.losses, 'go-', label='Training')
    plt.plot(epochs, val_metrics.losses, 'ro-', label='Validation')
    plt.title('LOSS')
    plt.legend()
    plt.show()


def print_metrics(train_metrics:MetricsReporter, val_metrics:MetricsReporter):
    data ={
        "tra acc": train_metrics.accuracies,
        "val acc": val_metrics.accuracies,
        "tra loss": train_metrics.losses,
        "val loss": val_metrics.losses,
    }
    df = pd.DataFrame(data)
    print(df.to_string(float_format=lambda n: format(n, '#.2g'), justify="right"))


def print_classification_reports(metrics:MetricsReporter):
    for report in metrics.classification_reports:
        print(report)

def print_confusion_matrices(metrics:MetricsReporter):
    for matrix in metrics.confusion_matrices:
        print_confusion_matrix(matrix, metrics.categories)

def print_confusion_matrix(confusion_matrix, categries):
    df = pd.DataFrame(confusion_matrix)
    df.columns = categries
    df.insert(0, "Pred/True", categries)
    df.set_index('Pred/True',inplace=True)
    print(df.to_string())
    print(os.linesep)