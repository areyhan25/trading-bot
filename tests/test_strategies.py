"""Tests for trading_bot.strategies."""

import pytest

from trading_bot.strategies import MovingAverageCrossover, Signal  # noqa: F401


@pytest.mark.skip(reason="TODO: implement MovingAverageCrossover first")
def test_ma_crossover_emits_buy_on_golden_cross(price_df):
    # TODO: Use small windows (e.g. 5/20) on a hand-built series where a cross
    #       happens on a known date; assert that row is Signal.BUY.
    # TODO: Also test: warm-up rows are HOLD, short >= long raises ValueError,
    #       latest_signal returns the last value of generate_signals.
    pass
