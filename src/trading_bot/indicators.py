"""Technical indicators as pure functions.

Every function takes a pandas Series (usually closing prices) and returns a
Series aligned to the same index. Early values that don't have enough history
should be NaN rather than dropped, so callers can line things up by date.
"""

from __future__ import annotations

import pandas as pd

from trading_bot import config


def sma(prices: pd.Series, window: int) -> pd.Series:
    """Simple moving average.

    SMA_t = mean(prices[t - window + 1 .. t])

    Args:
        prices: Price series (e.g. ``df["Close"]``).
        window: Number of periods to average. Must be >= 1.

    Returns:
        Series of the same length; the first ``window - 1`` values are NaN.

    Raises:
        ValueError: If ``window < 1``.
    """
    # TODO: Validate window.
    # TODO: Return prices.rolling(window=window).mean().
    raise NotImplementedError


def ema(prices: pd.Series, span: int) -> pd.Series:
    """Exponential moving average (more weight on recent prices).

    Smoothing factor alpha = 2 / (span + 1).

    Args:
        prices: Price series.
        span: EMA span. Must be >= 1.

    Returns:
        Series of the same length.

    Raises:
        ValueError: If ``span < 1``.
    """
    # TODO: Validate span.
    # TODO: Return prices.ewm(span=span, adjust=False).mean().
    # TODO: Decide whether to NaN-out the first span-1 values for consistency with sma().
    raise NotImplementedError


def rsi(prices: pd.Series, period: int = config.DEFAULT_RSI_PERIOD) -> pd.Series:
    """Relative Strength Index (Wilder's smoothing), scaled 0-100.

    Steps:
        1. delta = prices.diff()
        2. gains = delta clipped at 0 from below; losses = -delta clipped at 0
        3. avg_gain / avg_loss = Wilder-smoothed means
           (ewm with alpha = 1 / period, adjust=False)
        4. RS = avg_gain / avg_loss
        5. RSI = 100 - 100 / (1 + RS)

    Readings above ~70 are commonly read as "overbought", below ~30 as
    "oversold".

    Args:
        prices: Price series.
        period: Lookback period, classic default is 14.

    Returns:
        Series of RSI values in [0, 100]; the first ``period`` values are NaN.

    Raises:
        ValueError: If ``period < 1``.
    """
    # TODO: Validate period.
    # TODO: Implement steps 1-5 from the docstring.
    # TODO: Handle avg_loss == 0 (RSI should be 100, not inf/NaN).
    # TODO: Set the first `period` values to NaN (warm-up).
    raise NotImplementedError
