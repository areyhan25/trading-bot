"""Tests for trading_bot.indicators."""

import pytest

from trading_bot.indicators import ema, rsi, sma  # noqa: F401


@pytest.mark.skip(reason="TODO: implement indicators first")
def test_sma_matches_hand_calculation():
    # TODO: sma(pd.Series([1, 2, 3, 4, 5]), 3) -> [NaN, NaN, 2, 3, 4].
    # TODO: Also test: window < 1 raises ValueError, ema warm-up behavior,
    #       rsi stays within [0, 100], rsi == 100 on a strictly rising series.
    pass
