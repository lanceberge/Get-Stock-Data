<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
# Stock Data Retrieval

## Table of Contents

- [Stock Data Retrieval](#stock-data-retrieval)
    - [Example Use](#example-use)
    - [Dependencies](#dependencies)

<!-- markdown-toc end -->

## Example Use

```bash
$ python get.py GOOGL

GOOGL:
--------------------------------------------------------------------------------
Key Statistics:
---------------
Price:                2740.34
Market cap:           1.82T
EV/EBITDA:            21.16
Net Margins:          29.52%
Short Shares:         2.06M
P/B:                  7.45
P/S:                  None
forward PE:           24.38
Beta:                 1.07
Dividend Yield:       None

GOOGL:
--------------------------------------------------------------------------------
Balance Sheet:
--------------
                         2020-12-31 2019-12-31 2018-12-31 2017-12-31
Total Assets                319.62B    275.91B    232.79B    197.29B
Cash                         26.46B     18.50B     16.70B     10.71B
Intangible Assets             1.45B      1.98B      2.22B      2.69B
Inventories                 728.00M    999.00M      1.11B    749.00M
Total Liabilities            97.07B     74.47B     55.16B     44.79B
Long Term Debt               12.83B      3.96B      3.95B      3.94B
Total Shareholder Equity    222.54B    201.44B    177.63B    152.50B
```

## Dependencies

- pip install yahoofinancials
- pip install yfinance
- pip install pandas
- pip install numpy
