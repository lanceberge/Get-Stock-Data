import sys
from yahoofinancials import YahooFinancials
import yfinance as yf
from math log, floor
# import pandas_datareader as pdr

# from https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers
def millify(n):
    millnames = ['',' K',' M',' B',' T']

    n = float(n)
    k = 1000.0
    magnitude = int(floor(log(n, k)))
    return '%.2f%s' % (n / k**magnitude, units[magnitude])

    # millidx = max(0,min(len(millnames)-1,
    #                     int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    # return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def stock_info(ticker):
    print(ticker+": ")
    stock = yf.Ticker(ticker)
    symbol = YahooFinancials(ticker)

    print("Price: "     +str(symbol.get_current_price()))
    print("Market cap: "+str(millify(symbol.get_market_cap())))
    print("Dividend yield: "+"{:.2%}".format(symbol.get_dividend_yield()))

    print("Major Holders: ")
    print(stock.major_holders)

    print("Institutional: ")
    print(stock.institutional_holders)

    print("Balance Sheet: ")
    print(stock.balance_sheet)

    # TODO format - type is pd dataframe
    print("Quarterly: ")
    print(stock.quarterly_balance_sheet)

    print("Cash Flow: ")
    print(stock.cashflow)

    print("Quarterly: ")
    print(stock.quarterly_cashflow)

    print("Earnings: ")
    print(stock.earnings)

    print("Quarterly: ")
    print(stock.quarterly_earnings)

    print("Events: ")
    print(stock.calendar)

    # TODO could be useful
    # print("Info: ")
    # print(stock.info.items())

    # print("Price data: ")
    # print(stock.history(period="max"))

    # print("Actions: ")
    # print(stock.actions)

    # print("Dividends: ")
    # print(stock.dividends)

    # TODO could be useful
    # print("Financials: ")
    # print(stock.financials)
    # print("Quarterly: ")
    # print(stock.quarterly_financials)

    # TODO useful if formatted
    # print("News: ")
    # print(stock.news)

    ## balance sheet
    # long-term debt
    # cash
    # assets
    # liabilities

    # insider ownership
    # sales

    # volume
    # ev/ebitda

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
