#!/usr/bin/env python3

import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
import sys
from matplotlib import style


def chart(ticker):
    start = dt.datetime(2010, 1, 1)
    today = dt.datetime.now()
    df = pdr.get_data_yahoo(ticker, start, today)

    style.use('dark_background')
    plt.plot(df['Adj Close'])
    plt.show()


def main():
    for ticker in sys.argv[1:]:
        chart(ticker)


if __name__ == '__main__':
    main()
