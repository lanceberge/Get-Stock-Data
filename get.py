import sys
from math import log, floor
from yahoofinancials import YahooFinancials
import yfinance as yf
import pandas as pd
import numpy as np

# from https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers
def millify(n):
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
    if (n is None):
        return "N/A"

    return "{:.2%}".format(n)


def print_nums(titles, nums):
    for title, num in zip(titles, nums):
        # only use 2 decimal places of precision
        if (isinstance(num, float)):
            num = "%.2f" % num

        print("%-22s%-22s" % (title+': ', num))


def print_header(title, ticker):
    print('\n'+'-'*80)

    print(title+": \n")


# print the key statistics of a stock
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


# print a dataframe with given rows, updating its index to new_index,
# and applying func to all values element-wise if provided
def print_df(df, rows=None, new_index=None, func=None):

    # slice rows if provided
    if rows is not None:
        df = pd.DataFrame(df, index=rows)

    if new_index is not None:
        df.index = new_index

    if func is not None:
        df = df.applymap(func)

    print(df)


# output the key statistics, balance sheet, earnings, and cash flow
# of each ticker in sys.argv[1:]
def main():
    if len(sys.argv) == 1:
        print("expected at least one ticker symbol, terminating")
        return

    else:
        for ticker in sys.argv[1:]:
            print('\n'+ticker+": ")
            ticker = ticker.upper()
            key_statistics(ticker)

            stock = yf.Ticker(ticker)

            rows = ['Total Assets', 'Cash', 'Intangible Assets', 'Inventory',
                        'Total Liab', 'Long Term Debt', 'Total Stockholder Equity']

            new_index = ['Total Assets', 'Cash', 'Intangible Assets', 'Inventories',
                        'Total Liabilities', 'Long Term Debt',
                        'Total Shareholder Equity']

            print_header("Balance Sheet", ticker)
            print_df(stock.balance_sheet, rows=rows, new_index=new_index, func=millify)

            print("\nQuarterly:\n")
            print_df(stock.quarterly_balance_sheet, rows=rows,
                     new_index=new_index, func=millify)

            print_header("Earnings", ticker)
            print_df(stock.earnings, func=millify)

            print("\nQuarterly:\n")
            print_df(stock.quarterly_earnings, func=millify)

            rows = ["Total Cashflows From Investing Activities",
                    "Total Cash From Financing Activities",
                    "Total Cash From Operating Activities",
                    "Net Income", "Change In Cash",
                    "Repurchase Of Stock", "Capital Expenditures"]

            new_index = ["Investing Activities", "Financing Activities",
                         "Operating Activities", "Net Income", "Change In Cash",
                         "Repurchase of Stock", "Capital Expenditures"]

            print_header("Cash Flow", ticker)
            print_df(stock.cashflow, rows=rows, new_index=new_index, func=millify)

            print("\nQuarterly:\n")
            print_df(stock.quarterly_cashflow, rows=rows, new_index=new_index, func=millify)


if __name__ == "__main__":
    main()
