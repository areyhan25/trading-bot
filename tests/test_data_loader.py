"""Tests for trading_bot.data_loader."""

import pytest

from trading_bot.data_loader import PriceDataLoader  # noqa: F401


@pytest.mark.skip(reason="TODO: implement PriceDataLoader first")
def test_get_prices_uses_fresh_cache(tmp_path, price_df):
    # TODO: Save price_df into tmp_path via save_cache, then call get_prices
    #       and assert fetch() was NOT called (monkeypatch it to raise).
    # TODO: Also test: stale cache triggers fetch, _clean flattens columns,
    #       _validate raises DataLoaderError on missing columns.
    pass
