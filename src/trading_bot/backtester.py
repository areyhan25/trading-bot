"""Run a strategy over historical data and report simple performance stats.

Simplifying assumptions (document any you change):
    - Long-only: either fully invested or fully in cash.
    - BUY when flat -> go all-in at the *next* bar's Open (avoids look-ahead).
    - SELL when long -> exit fully at the next bar's Open.
    - BUY while already long, or SELL while flat, is ignored.
    - No commissions, slippage, taxes, dividends handling, or shorting.
    - Any open position is valued at the final Close (not force-sold).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from trading_bot import config
from trading_bot.strategies.base import Strategy


@dataclass
class Trade:
    """One completed round trip (entry -> exit)."""

    entry_date: pd.Timestamp
    entry_price: float
    exit_date: pd.Timestamp
    exit_price: float

    @property
    def return_pct(self) -> float:
        """Percent return of this trade, e.g. 0.05 for +5%."""
        # TODO: Return (exit_price - entry_price) / entry_price.
        raise NotImplementedError


@dataclass
class BacktestResult:
    """Summary of a backtest run.

    Attributes:
        ticker: Symbol tested.
        strategy_name: ``Strategy.describe()`` output.
        start: First date in the test window.
        end: Last date in the test window.
        initial_cash: Starting portfolio value.
        final_value: Ending portfolio value.
        total_return: Strategy return over the period (0.10 == +10%).
        buy_and_hold_return: Return from buying on day 1 and holding (benchmark).
        max_drawdown: Worst peak-to-trough drop of the equity curve (negative number).
        win_rate: Fraction of completed trades with a positive return (0..1).
        num_trades: Number of completed round trips.
        equity_curve: Portfolio value per bar.
        trades: List of completed trades.
    """

    ticker: str
    strategy_name: str
    start: pd.Timestamp
    end: pd.Timestamp
    initial_cash: float
    final_value: float
    total_return: float
    buy_and_hold_return: float
    max_drawdown: float
    win_rate: float
    num_trades: int
    equity_curve: pd.Series = field(repr=False)
    trades: list[Trade] = field(default_factory=list, repr=False)

    def summary(self) -> str:
        """Human-readable multi-line report for the CLI.

        Should include: ticker, strategy, date range, total return vs.
        buy-and-hold, max drawdown, win rate, and number of trades.
        Format percentages like ``+12.34%``.
        """
        # TODO: Build and return a formatted string.
        raise NotImplementedError


class Backtester:
    """Simulates a long-only strategy on historical OHLCV data.

    Args:
        initial_cash: Starting portfolio value.
    """

    def __init__(self, initial_cash: float = config.DEFAULT_INITIAL_CASH) -> None:
        # TODO: Validate initial_cash > 0 and store it.
        pass

    def run(self, df: pd.DataFrame, strategy: Strategy, ticker: str = "") -> BacktestResult:
        """Backtest ``strategy`` on ``df``.

        Steps:
            1. signals = strategy.generate_signals(df)
            2. Walk forward bar by bar. When a signal appears on bar t, execute
               at bar t+1's Open (see module docstring for rules).
            3. Track cash, shares held, and portfolio value each bar
               (value = cash + shares * Close) to build the equity curve.
            4. Record a Trade on each completed exit.
            5. Compute stats with the helper functions below.
            6. Return a BacktestResult.

        Args:
            df: OHLCV DataFrame.
            strategy: Any :class:`Strategy` instance.
            ticker: Optional symbol, only used for reporting.

        Returns:
            A populated :class:`BacktestResult`.

        Raises:
            ValueError: If ``df`` has fewer rows than ``strategy.min_history()``.
        """
        # TODO: Implement steps 1-6.
        raise NotImplementedError


def total_return(equity_curve: pd.Series) -> float:
    """Return (last / first) - 1 for an equity or price series."""
    # TODO: Implement; guard against empty series.
    raise NotImplementedError


def buy_and_hold_return(df: pd.DataFrame) -> float:
    """Benchmark: buy at the first Open, value at the last Close."""
    # TODO: Return df["Close"].iloc[-1] / df["Open"].iloc[0] - 1.
    raise NotImplementedError


def max_drawdown(equity_curve: pd.Series) -> float:
    """Largest peak-to-trough decline as a negative fraction (e.g. -0.25).

    Steps:
        1. running_peak = equity_curve.cummax()
        2. drawdown = equity_curve / running_peak - 1
        3. return drawdown.min()
    """
    # TODO: Implement steps 1-3.
    raise NotImplementedError


def win_rate(trades: list[Trade]) -> float:
    """Fraction of trades with return_pct > 0. Return 0.0 if there are no trades."""
    # TODO: Implement.
    raise NotImplementedError
