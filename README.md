<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
# Stock Data Retrieval

Retrieve various fundamental metrics for a stock

*Note*: Some of the reported values may be wrong due to the APIs. I've only noticed this so far with foreign stocks, for example the yahoofinancials API thinks BABA has a EV/EBITDA of 1.31.


## Table of Contents

- [Stock Data Retrieval](#stock-data-retrieval)
    - [Example Use](#example-use)
    - [Dependencies](#dependencies)

<!-- markdown-toc end -->

## Example Use

```bash
$ ./get.py GOOGL -q # -q shows quarterly stats

GOOGL:

--------------------------------------------------------------------------------
Key Statistics:

Price:                2740.34
Market cap:           1.82T
EV/EBITDA:            20.01
Net Margins:          29.52%
P/B:                  7.45
P/S:                  7.60
forward PE:           24.38
Beta:                 1.06
Dividend Yield:       N/A

--------------------------------------------------------------------------------
Balance Sheet:

                         2020-12-31 2019-12-31 2018-12-31 2017-12-31
Total Assets                319.62B    275.91B    232.79B    197.29B
Cash                         26.46B     18.50B     16.70B     10.71B
Intangible Assets             1.45B      1.98B      2.22B      2.69B
Inventories                 728.00M    999.00M      1.11B    749.00M
Total Liabilities            97.07B     74.47B     55.16B     44.79B
Long Term Debt               12.83B      3.96B      3.95B      3.94B
Total Shareholder Equity    222.54B    201.44B    177.63B    152.50B

Quarterly:

                         2021-09-30 2021-06-30 2021-03-31 2020-12-31
Total Assets                347.40B    335.39B    327.10B    319.62B
Cash                         23.72B     23.63B     26.62B     26.46B
Intangible Assets             1.55B      1.63B      1.82B      1.45B
Inventories                   1.28B    907.00M    888.00M    728.00M
Total Liabilities           102.84B     97.82B     97.08B     97.07B
Long Term Debt               12.84B     12.84B     12.84B     12.83B
Total Shareholder Equity    244.57B    237.56B    230.01B    222.54B

--------------------------------------------------------------------------------
Earnings:

      Revenue Earnings
Year
2017  110.86B   12.66B
2018  136.82B   30.74B
2019  161.86B   34.34B
2020  182.53B   40.27B

Quarterly:

        Revenue Earnings
Quarter
4Q2020   56.90B   15.23B
1Q2021   55.31B   17.93B
2Q2021   61.88B   18.52B
3Q2021   65.12B   18.94B

--------------------------------------------------------------------------------
Cash Flow:

                     2020-12-31 2019-12-31 2018-12-31 2017-12-31
Investing Activities    -32.77B    -29.49B    -28.50B    -31.40B
Financing Activities    -24.41B    -23.21B    -13.18B     -8.30B
Operating Activities     65.12B     54.52B     47.97B     37.09B
Net Income               40.27B     34.34B     30.74B     12.66B
Change In Cash            7.97B      1.80B      5.99B     -2.20B
Repurchase of Stock     -31.15B    -18.40B     -9.07B     -4.85B
Capital Expenditures    -22.28B    -23.55B    -25.14B    -13.18B

Quarterly:

                     2021-09-30 2021-06-30 2021-03-31 2020-12-31
Investing Activities    -10.05B     -9.07B     -5.38B     -7.28B
Financing Activities    -15.25B    -15.99B    -13.61B     -9.27B
Operating Activities     25.54B     21.89B     19.29B     22.68B
Net Income               18.94B     18.52B     17.93B     15.23B
Change In Cash           89.00M     -2.99B    157.00M      6.34B
Repurchase of Stock     -12.61B    -12.80B    -11.39B     -7.90B
Capital Expenditures     -6.82B     -5.50B     -5.94B     -5.48B
```

You can see quarterly breakdowns with the `-q` flag. You can choose which metrics to see
with the `--metrics` flag (default metrics=all). The `--metrics` flag is aliases
to `-m`. For example:

```
# All of these are equivalent:
$ ./get.py GOOGL -qmkbeq
$ ./get.py GOOGL -q --metrics=kbeq
$ ./get.py GOOGL -q --metrics=key_stats,balance_sheet,earnings,cash_flow
```

## Dependencies

| Name            |
|--               |
| yahoofinancials |
| yfinance        |
| pandas          |
| numpy           |

```
$ pip install yahoofinancials yfinance pandas numpy
```
