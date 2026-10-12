"""trading_bot: a historical-data trading *suggestion* tool.

Reads historical prices from Yahoo Finance (via ``yfinance``), computes
technical indicators, runs rules-based strategies, and prints BUY / SELL / HOLD
suggestions. It never connects to a brokerage, never uses live data feeds, and
never places trades.

Not financial advice.
"""

__version__ = "0.1.0"
