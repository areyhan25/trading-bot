"""Moving-average crossover strategy."""

from __future__ import annotations

import pandas as pd

from trading_bot import config
from trading_bot.strategies.base import Signal, Strategy


class MovingAverageCrossover(Strategy):
    """Classic two-SMA crossover.

    Rules:
        - BUY on the bar where the short SMA crosses *above* the long SMA
          ("golden cross"): short[t-1] <= long[t-1] and short[t] > long[t].
        - SELL on the bar where the short SMA crosses *below* the long SMA
          ("death cross"): short[t-1] >= long[t-1] and short[t] < long[t].
        - HOLD on every other bar, including warm-up bars where either SMA is NaN.

    Args:
        short_window: Lookback for the fast SMA.
        long_window: Lookback for the slow SMA. Must be greater than ``short_window``.

    Raises:
        ValueError: If windows are < 1 or ``short_window >= long_window``.
    """

    name = "ma"

    def __init__(
        self,
        short_window: int = config.DEFAULT_SHORT_WINDOW,
        long_window: int = config.DEFAULT_LONG_WINDOW,
    ) -> None:
        # TODO: Validate the windows (see Raises above).
        # TODO: Store them on self.
        pass

    def generate_signals(self, df: pd.DataFrame) -> pd.Series:
        """Return BUY/SELL/HOLD for each row based on SMA crossovers.

        Steps:
            1. short = indicators.sma(df["Close"], self.short_window)
            2. long = indicators.sma(df["Close"], self.long_window)
            3. above = short > long  (bool Series)
            4. crossed_up = above & ~above.shift(1, fill_value=False)
               crossed_down = ~above & above.shift(1, fill_value=False)
            5. Start from a Series of Signal.HOLD, set BUY where crossed_up,
               SELL where crossed_down.
            6. Force HOLD wherever short or long is NaN (warm-up period).
        """
        # TODO: Implement steps 1-6.
        raise NotImplementedError

    def min_history(self) -> int:
        """Need ``long_window + 1`` rows to detect the first possible crossover."""
        # TODO: Return self.long_window + 1.
        raise NotImplementedError

    def describe(self) -> str:
        """E.g. ``"MA crossover (50/200)"``."""
        # TODO: Return a formatted string using the windows.
        raise NotImplementedError
