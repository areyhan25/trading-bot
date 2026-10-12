"""Base types every strategy builds on."""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum

import pandas as pd


class Signal(str, Enum):
    """A strategy's suggestion for a single bar.

    Subclassing ``str`` makes values print nicely and compare to plain strings.
    """

    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


class Strategy(ABC):
    """Abstract base class for rules-based strategies.

    A strategy is stateless with respect to data. It receives a full OHLCV
    DataFrame and returns one :class:`Signal` per row. Parameters (window
    sizes, thresholds) are set in ``__init__``.

    Important: signals for row ``t`` may only use data up to and including
    row ``t``. Peeking at future rows (look-ahead bias) makes backtests lie.
    """

    #: Short human-readable name, shown in CLI output. Override in subclasses.
    name: str = "base"

    @abstractmethod
    def generate_signals(self, df: pd.DataFrame) -> pd.Series:
        """Compute a signal for every row of ``df``.

        Args:
            df: OHLCV DataFrame from :class:`~trading_bot.data_loader.PriceDataLoader`.

        Returns:
            Series indexed like ``df`` whose values are :class:`Signal`
            members. Rows without enough history should be ``Signal.HOLD``.
        """
        raise NotImplementedError

    def latest_signal(self, df: pd.DataFrame) -> Signal:
        """Return the signal for the most recent bar in ``df``.

        Args:
            df: OHLCV DataFrame.

        Returns:
            The last value of :meth:`generate_signals`.
        """
        # TODO: Call self.generate_signals(df) and return the last element.
        # TODO: Raise ValueError if df is empty.
        raise NotImplementedError

    def min_history(self) -> int:
        """Minimum number of rows needed before signals are meaningful.

        Used to warn the user (or raise) when there isn't enough data.
        Subclasses should override this. The default of 1 means "no warm-up".
        """
        return 1

    def describe(self) -> str:
        """One-line description including parameters, e.g. ``"MA crossover (50/200)"``."""
        # TODO: Return a readable string; subclasses can override for more detail.
        raise NotImplementedError

    def __repr__(self) -> str:
        # TODO: Return something like f"{self.__class__.__name__}(...params...)".
        return f"{self.__class__.__name__}()"
