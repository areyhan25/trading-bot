"""Tests for trading_bot.backtester."""

import pytest

from trading_bot.backtester import Backtester, max_drawdown  # noqa: F401


@pytest.mark.skip(reason="TODO: implement Backtester first")
def test_max_drawdown_on_known_curve():
    # TODO: max_drawdown(pd.Series([100, 120, 90, 130])) == 90/120 - 1 == -0.25.
    # TODO: Also test: a strategy that always HOLDs ends with initial_cash,
    #       trades execute at the NEXT bar's Open, win_rate with no trades is 0.0.
    pass
