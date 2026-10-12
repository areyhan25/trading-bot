"""Shared pytest fixtures. No network access: tests use synthetic data."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def price_df() -> pd.DataFrame:
    """300 business days of fake OHLCV data with a gentle up-then-down trend.

    Long enough for a 50/200 SMA crossover strategy to warm up.
    """
    rng = np.random.default_rng(seed=42)
    dates = pd.bdate_range("2024-01-01", periods=300)
    trend = np.concatenate([np.linspace(100, 150, 150), np.linspace(150, 110, 150)])
    close = trend + rng.normal(0, 1.0, size=len(dates))
    return pd.DataFrame(
        {
            "Open": close + rng.normal(0, 0.5, size=len(dates)),
            "High": close + 1.0,
            "Low": close - 1.0,
            "Close": close,
            "Volume": rng.integers(1_000_000, 5_000_000, size=len(dates)),
        },
        index=dates,
    )
