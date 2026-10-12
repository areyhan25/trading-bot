"""Tests for trading_bot.suggestion."""

import pytest

from trading_bot.suggestion import DISCLAIMER, generate_suggestion  # noqa: F401


@pytest.mark.skip(reason="TODO: implement generate_suggestion first")
def test_generate_suggestion_with_fake_loader(price_df):
    # TODO: Build a fake loader whose get_prices returns price_df, pass it in,
    #       and assert the Suggestion's as_of == price_df.index[-1].
    # TODO: Also test: too little history raises ValueError,
    #       Suggestion.format() contains DISCLAIMER.
    pass
