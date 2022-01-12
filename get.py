import sys
from math import log, floor
from yahoofinancials import YahooFinancials
import yfinance as yf
import pandas as pd
import numpy as np

# from https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers
def millify(n):
    """Convert a number from 1000 -> 1K, 1000000 -> 1M, etc."""
    if n is None or np.isnan(n):
        return "N/A"

    units = ['','K','M','B','T']

    n = float(n)

    k = 1000.0
    magnitude = int(floor(log(abs(n), k)))

    if n < 0:
        return '-%.2f%s' % (-n / k**magnitude, units[magnitude])

    return '%.2f%s' % (n / k**magnitude, units[magnitude])


# format a float as a percent
def format_percent(n):
    """Format a float as a percent"""
    if (n is None):
        return "N/A"

    return "{:.2%}".format(n)


def print_nums(titles, nums):
    """Print numbers with aligned columns (titles and nums)"""
    for title, num in zip(titles, nums):
        # only use 2 decimal places of precision
        if (isinstance(num, float)):
            num = "%.2f" % num

        print("%-22s%-22s" % (title+': ', num))


# print a dataframe with given rows, updating its index to new_index
def print_df(df, rows=None, names=None):
    """Print a millified dataframe, using only the rows in rows"""
    # slice rows if provided
    if rows is not None:
        df = pd.DataFrame(df, index=rows)

    if names is not None:
        df.index = names

    df = df.applymap(millify)

    print(df)


def print_header(title, ticker):
    """print a heading"""
    print('\n'+'-'*80)

    print(title+": \n")


def key_statistics(ticker):
    """Print the key statistics of a stock"""

    stock = YahooFinancials(ticker)

    print_header("Key Statistics", ticker)

    # the names of what will be outputted
    names = ["Price"                   , "Market cap"]

    # the values corresponding to each name
    vals  = [stock.get_current_price(), millify(stock.get_market_cap())]

    # get the key statistics dictionary from YahooFinancials
    dict = stock.get_key_statistics_data().get(ticker)

    # update data to correct format
    dict.update({'profitMargins': format_percent(dict.get('profitMargins'))})

    # keys in the dict we want to output
    dict_keys = ["enterpriseToEbitda", "profitMargins", "priceToBook"]
    names    += ["EV/EBITDA"         , "Net Margins"  , "P/B"]

    # add values from the dictionary to vals
    vals += [dict.get(key) for key in dict_keys]

    names += ["P/S"]
    vals  += [stock.get_price_to_sales()]

    dict_keys = ["forwardPE" , "beta"]
    names    += ["forward PE", "Beta"]

    # add values from the dictionary to vals
    vals += [dict.get(key) for key in dict_keys]

    names += ["Dividend Yield"]
    vals  += [format_percent(stock.get_dividend_yield())]

    print_nums(names, vals)


# output the key statistics, balance sheet, earnings, and cash flow
def print_balance_sheet(stock, ticker, quarterly=False):
    """print a stock's balance sheet"""

    rows  = ['Total Assets', 'Cash', 'Intangible Assets', 'Inventory',
             'Total Liab', 'Long Term Debt', 'Total Stockholder Equity']

    names = ['Total Assets', 'Cash', 'Intangible Assets', 'Inventories',
            'Total Liabilities', 'Long Term Debt',
            'Total Shareholder Equity']

    print_header("Balance Sheet", ticker)
    print_df(stock.balance_sheet, rows, names)

    if quarterly:
        print("\nQuarterly:\n")
        print_df(stock.quarterly_balance_sheet, rows, names)


def print_earnings(stock, ticker, quarterly=False):
    """print a stock's earnings statement"""

    print_header("Earnings", ticker)
    print_df(stock.earnings)

    if quarterly:
        print("\nQuarterly:\n")
        print_df(stock.quarterly_earnings)


def print_cashflow(stock, ticker, quarterly=False):
    """print a stock's cashflow statement"""

    rows = ["Total Cashflows From Investing Activities",
            "Total Cash From Financing Activities",
            "Total Cash From Operating Activities",
            "Net Income", "Change In Cash",
            "Repurchase Of Stock", "Capital Expenditures"]

    names = ["Investing Activities", "Financing Activities",
             "Operating Activities", "Net Income", "Change In Cash",
             "Repurchase of Stock", "Capital Expenditures"]

    print_header("Cash Flow", ticker)
    print_df(stock.cashflow, rows, names)

    if quarterly:
        print("\nQuarterly:\n")
        print_df(stock.quarterly_cashflow, rows, names)


# of each ticker in sys.argv[1:]
def main():
    """parse command line args and output statistics accordingly"""

    if len(sys.argv) == 1:
        print("expected at least one ticker symbol, terminating")
        return

    all_metrics = True
    quarterly   = False

    # parse all the args that are flags
    for arg in sys.argv[1:]:

        if arg[0] != '-':
            continue

        if 'q' in arg:
            quarterly = True

        # if the arg contains --metrics=
        if arg.startswith('--metrics=') or 'm' in arg:
            if (arg.startswith('--metrics')):
                metrics = arg.split('=')[1]

            else:
                metrics = arg[2:]

            if 'all' in metrics:
                all_metrics=True

            else:
                all_metrics = False

                key_stats     = 'k' in metrics or 'key_stats'     in metrics
                balance_sheet = 'b' in metrics or 'balance_sheet' in metrics
                earnings      = 'e' in metrics or 'earnings'      in metrics
                cash_flow     = 'c' in metrics or 'cash_flow'     in metrics

    # parse all the args that aren't flags
    for arg in sys.argv[1:]:
        if arg[0] == '-':
            continue

        ticker = arg.upper()

        # initial heading
        print('\n'+ticker+": ")

        stock = yf.Ticker(ticker)

        # call the metrics
        if all_metrics:
            key_statistics(ticker)
            print_balance_sheet(stock, ticker, quarterly)
            print_earnings(stock, ticker, quarterly)
            print_cashflow(stock, ticker, quarterly)

        else:
            if key_stats:
                key_statistics(ticker)

            if balance_sheet:
                print_balance_sheet(stock, ticker, quarterly)

            if earnings:
                print_earnings(stock, ticker, quarterly)

            if cash_flow:
                print_cashflow(stock, ticker, quarterly)


if __name__ == "__main__":
    main()
