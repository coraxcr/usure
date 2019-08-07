import os
from typing import Iterable
import matplotlib.pyplot as plt
from matplotlib import markers 
import pandas as pd
from functools import reduce
from usure.classification.core import Metrics, LabReport, ModelReport


def _model_report_to_dict(model_report:ModelReport)-> pd.DataFrame:
    report = {
        "model name" : model_report.name,
        "train_acc" : model_report.training.accuracy,
        "val_acc" : model_report.validation.accuracy,
        "train_loss" : model_report.training.loss,
        "val_loss" : model_report.validation.loss       
    }
    return report

def model_reports_to_DataFrame(model_reports:Iterable[ModelReport])-> pd.DataFrame:
    model_reports_dicts = list(map(lambda model_report: _model_report_to_dict(model_report), model_reports))
    model_report_df =  pd.DataFrame(model_reports_dicts)
    #model_report_df = model_report_df[["model name", "train_acc", "val_acc", "train_loss", "val_loss"]]
    return model_report_df

def plot_learning_curves(model_reports:Iterable[ModelReport]):
    model_reports_df = model_reports_to_DataFrame(model_reports)
    f, ax = plt.subplots(1, 2, figsize = (16, 7))
    no_epochs = range(1, len(model_reports) + 1)
    plt.sca(ax[0])
    plt.plot(no_epochs, model_reports_df["train_acc"], 'go-', label='Training')
    plt.plot(no_epochs, model_reports_df["val_acc"], 'ro-', label='Validation')
    plt.title('ACCURACY')
    plt.legend()
    plt.sca(ax[1])
    plt.plot(no_epochs, model_reports_df["val_loss"], 'ro-', label='Validation')
    plt.plot(no_epochs, model_reports_df["train_loss"], 'go-', label='Training')
    plt.title('LOSS')
    plt.legend()
    plt.show()

def plot_learning_curves_if_epoches(model_report:ModelReport):
    model_reports_epochs = model_report.epochs
    if model_reports_epochs:
        plot_learning_curves(model_reports_epochs)