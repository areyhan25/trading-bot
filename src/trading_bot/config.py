"""Project-wide defaults.

Keep tunable constants here so the rest of the code never hard-codes paths
or magic numbers. Everything in this module should be plain values, with no logic.
"""

from __future__ import annotations

from pathlib import Path

# Repo root is three levels up from this file: src/trading_bot/config.py
PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

# Where downloaded price data is cached between runs (gitignored).
CACHE_DIR: Path = PROJECT_ROOT / "data" / "cache"

# How long a cached file is considered fresh before re-downloading.
CACHE_MAX_AGE_HOURS: int = 24

# Default yfinance query parameters.
DEFAULT_PERIOD: str = "2y"  # e.g. "1y", "2y", "5y", "max"
DEFAULT_INTERVAL: str = "1d"  # daily bars

# Default moving-average crossover windows (classic "golden cross" setup).
DEFAULT_SHORT_WINDOW: int = 50
DEFAULT_LONG_WINDOW: int = 200

# Default RSI settings.
DEFAULT_RSI_PERIOD: int = 14
RSI_OVERBOUGHT: float = 70.0
RSI_OVERSOLD: float = 30.0

# Backtest defaults.
DEFAULT_INITIAL_CASH: float = 10_000.0
TRADING_DAYS_PER_YEAR: int = 252
