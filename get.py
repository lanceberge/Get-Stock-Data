import sys
from math import log, floor
from yahoofinancials import YahooFinancials
import yfinance as yf
import pandas as pd
import numpy as np

# from https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers
def millify(n):
    if n is None or np.isnan(n):
        return "NaN"

    units = ['','K','M','B','T']

    n = float(n)
    k = 1000.0
    magnitude = int(floor(log(n, k)))
    return '%.2f%s' % (n / k**magnitude, units[magnitude])


def format_percent(n):
    if (n is None):
        return "None"

    return "{:.2%}".format(n)


def print_nums(titles, nums):
    for title, num in zip(titles, nums):
        # only use 2 decimal places of precision
        if (isinstance(num, float)):
            num = "%.2f" % num

        print("%-22s%-22s" % (title+': ', num))


def print_header(title, ticker):
    print('\n'+ticker+": ")
    print('-'*80)

    print(title+": ")
    print('-'*(len(title)+1))


def key_statistics(ticker):
    stock = yf.Ticker(ticker)
    symbol = YahooFinancials(ticker)

    print_header("Key Statistics", ticker)

    names = ["Price"                   , "Market cap"]
    vals  = [symbol.get_current_price(), millify(symbol.get_market_cap())]

    # get the key statistics dictionary from YahooFinancials
    dict = symbol.get_key_statistics_data().get(ticker)

    rownames = ["enterpriseToEbitda", "profitMargins", "sharesShort" , "priceToBook"]
    names   += ["EV/EBITDA"         , "Net Margins"  , "Short Shares", "P/B"]

    rownames += ["priceToSalesTrailing12Months", "forwardPE" , "beta"]
    names    += ["P/S"                         , "forward PE", "Beta"]

    # update data to correct format
    dict.update({'profitMargins': format_percent(dict.get('profitMargins'))})
    dict.update({'sharesShort': millify(dict.get('sharesShort'))})

    # add values from the dictionary to vals
    vals += [dict.get(row) for row in rownames]

    names += ["Dividend Yield"]
    vals  += [format_percent(symbol.get_dividend_yield())]

    print_nums(names, vals)


def balance_sheet(ticker):
    print_header("Balance Sheet", ticker)

    stock = yf.Ticker(ticker)
    symbol = YahooFinancials(ticker)

    colnames = ['Total Assets', 'Cash', 'Intangible Assets', 'Inventory',
                'Total Liab', 'Long Term Debt', 'Total Stockholder Equity']

    df = stock.balance_sheet
    df = pd.DataFrame(df, index=colnames)

    # Update column names
    colnames = ['Total Assets', 'Cash', 'Intangible Assets', 'Inventories',
                'Total Liabilities', 'Long Term Debt',
                'Total Shareholder Equity']

    df.index = colnames

    df = df.applymap(millify)
    print(df)


def main():
    if len(sys.argv) == 1:
        print("expected at least one ticker symbol, terminating")
        return

    else:
        for ticker in sys.argv[1:]:
            ticker = ticker.upper()
            key_statistics(ticker)
            balance_sheet(ticker)


if __name__ == "__main__":
    main()
