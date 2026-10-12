"""Turn the latest strategy signal into a user-facing suggestion."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from trading_bot.data_loader import PriceDataLoader
from trading_bot.strategies.base import Signal, Strategy

DISCLAIMER = (
    "Educational tool only, not financial advice. "
    "Based on historical data; past performance does not predict future results."
)


@dataclass(frozen=True)
class Suggestion:
    """A single BUY / SELL / HOLD suggestion for a ticker.

    Attributes:
        ticker: Symbol the suggestion is for.
        signal: The suggested action.
        as_of: Date of the last bar used (not "today": data may lag).
        last_close: Closing price on ``as_of``.
        strategy_name: Which strategy produced it (``Strategy.describe()``).
        reason: Short plain-English explanation, e.g.
            "50-day SMA crossed above 200-day SMA".
    """

    ticker: str
    signal: Signal
    as_of: pd.Timestamp
    last_close: float
    strategy_name: str
    reason: str = ""

    def format(self) -> str:
        """Pretty multi-line string for terminal output, ending with :data:`DISCLAIMER`."""
        # TODO: Build a readable block, e.g.
        #   AAPL  ->  HOLD
        #   as of 2026-10-09 | close $231.40
        #   strategy: MA crossover (50/200)
        #   reason: no crossover on the latest bar
        #   <DISCLAIMER>
        raise NotImplementedError


def generate_suggestion(
    ticker: str,
    strategy: Strategy,
    loader: PriceDataLoader | None = None,
    period: str | None = None,
) -> Suggestion:
    """Load data for ``ticker``, run ``strategy``, and package the latest signal.

    Args:
        ticker: Symbol, e.g. ``"AAPL"``.
        strategy: Any configured :class:`Strategy`.
        loader: Optional loader (inject a fake one in tests). Defaults to a new
            :class:`PriceDataLoader`.
        period: Optional yfinance period override; must give the strategy
            at least ``strategy.min_history()`` rows.

    Returns:
        A :class:`Suggestion` for the most recent bar.

    Raises:
        ValueError: If there's not enough history for the strategy.
    """
    # TODO: loader = loader or PriceDataLoader().
    # TODO: df = loader.get_prices(ticker, period=...) (only pass period if given).
    # TODO: Check len(df) >= strategy.min_history(), else raise ValueError.
    # TODO: signal = strategy.latest_signal(df).
    # TODO: Build reason text with explain_signal(...).
    # TODO: Return Suggestion(ticker, signal, df.index[-1], df["Close"].iloc[-1], strategy.describe(), reason).
    raise NotImplementedError


def explain_signal(signal: Signal, strategy: Strategy) -> str:
    """Return a short plain-English reason for ``signal`` given ``strategy``.

    Keep it generic for now (e.g. map each Signal to a sentence). Later you
    could let each Strategy provide its own explanation.
    """
    # TODO: Return a sentence per Signal value.
    raise NotImplementedError
