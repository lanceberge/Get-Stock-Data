<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
# Stock Data Retrieval

## Table of Contents

- [Stock Data Retrieval](#stock-data-retrieval)
    - [Example Use](#example-use)
    - [Dependencies](#dependencies)

<!-- markdown-toc end -->

## Example Use

```bash
$ python get.py AMZN GOOGL

AMZN:
--------------------------------------------------------------------------------
Key Statistics:
---------------
Price:                3251.08
Market cap:           1.65T
EV / EBITDA:          28.244
Net Margins:          5.74%
Short Shares:         3.60M
P/B:                  13.671547
P/S:                  None
forward PE:           63.09102
Beta:                 1.095793
Dividend Yield:       None

GOOGL:
--------------------------------------------------------------------------------
Key Statistics:
---------------
Price:                2740.34
Market cap:           1.82T
EV / EBITDA:          20.013
Net Margins:          29.52%
Short Shares:         2.06M
P/B:                  7.447669
P/S:                  None
forward PE:           24.375914
Beta:                 1.058286
Dividend Yield:       None
~/code/stock_data #
```

## Dependencies

- pip install yahoofinancials
- pip install yfinance
