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
P/B:                  13.67
P/S:                  None
forward PE:           63.09
Beta:                 1.10
Dividend Yield:       None

GOOGL:
--------------------------------------------------------------------------------
Key Statistics:
---------------
Price:                2740.34
Market cap:           1.82T
EV / EBITDA:          20.01
Net Margins:          29.52%
Short Shares:         2.06M
P/B:                  7.45
P/S:                  None
forward PE:           24.40
Beta:                 1.06
Dividend Yield:       None
```

## Dependencies

- pip install yahoofinancials
- pip install yfinance
