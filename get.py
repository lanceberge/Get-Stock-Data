import sys
from yahoofinancials import YahooFinancials
import yfinance as yf
from math import log, floor
import pandas as pd
# import pandas_datareader as pdr

# from https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers
def millify(n):
    units = ['',' K',' M',' B',' T']

    n = float(n)
    k = 1000.0
    magnitude = int(floor(log(n, k)))
    return '%.2f%s' % (n / k**magnitude, units[magnitude])

def format_percent(n):
    return "{:.2%}".format(n)

def print_items_in_dict(dict, items, names):
    for item, name in zip(items, names):
        val = dict.get(item)
        print(f"{name}: {val}")

def stock_info(ticker):
    stock = yf.Ticker(ticker)
    symbol = YahooFinancials(ticker)

    print(ticker+": ")

    print("Key Statistics: ")
    dict = symbol.get_key_statistics_data().get(ticker)
    items = ["enterpriseToEbitda", "profitMargins", "sharesShort" , "priceToBook"]
    names = ["EV / EBITDA"       , "Net Margins"  , "Short Shares", "P/B"]

    items += ["priceToSalesTrailing12Months", "forwardPE" , "beta"]
    names += ["P/S"                         , "forward PE", "Beta"]

    dict.update({'profitMargins': format_percent(dict.get('profitMargins'))})
    dict.update({'sharesShort': millify(dict.get('sharesShort'))})

    print_items_in_dict(dict, items, names)

    ev = dict.get("enterpriseValue")

    print("Price: "         +str(symbol.get_current_price()))
    print("Market cap: "    +str(millify(symbol.get_market_cap())))
    print("Dividend yield: "+format_percent(symbol.get_dividend_yield()))

    # print("\nBalance Sheet: ")
    # print(stock.balance_sheet)

    # print("Quarterly: ")
    # print(stock.quarterly_balance_sheet)

    # print("Cash Flow: ")
    # print(stock.cashflow)

    # print("Quarterly: ")
    # print(stock.quarterly_cashflow)

    # print("Earnings: ")
    # print(stock.earnings)

    # print("Quarterly: ")
    # print(stock.quarterly_earnings)

    # print("Events: ")
    # print(stock.calendar)

    # print("Major Holders: ")
    # print(stock.major_holders)

    # print("Institutional: ")
    # print(stock.institutional_holders)

    # print("Info: ")
    # print(stock.info.items())

    # print("Price data: ")
    # print(stock.history(period="max"))

    # print("Actions: ")
    # print(stock.actions)

    # print("Dividends: ")
    # print(stock.dividends)

    # print("Financials: ")
    # print(stock.financials)
    # print("Quarterly: ")
    # print(stock.quarterly_financials)

    # print("News: ")
    # print(stock.news)

    ## over time data
    # print(pdr.get_data_yahoo(ticker))
    # data = yf.ticker(ticker).history(period='5y')

def main():
    if len(sys.argv) == 1:
        print("expected at least one ticker symbol, terminating")
        return
    else:
        for ticker in sys.argv[1:]:
            stock_info(ticker.upper())


if __name__ == "__main__":
    main()
