import numpy as np
import pandas as pd
import pickle


def process_data_for_labels(ticker):
    days = 7
    df = pd.read_csv('sp500_join_closes.csv', index_col=0)
    tickers = df.columns.values
    df.fillna(0, inplace=True)

    for i in range(1, days + 1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df


process_data_for_labels('XOM')
