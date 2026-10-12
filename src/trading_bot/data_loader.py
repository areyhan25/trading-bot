"""Fetch and cache historical price data from Yahoo Finance.

This is the only module that talks to the network. Everything downstream
works on the pandas DataFrame it returns, so it can be tested offline with
synthetic data.

Expected DataFrame shape returned by :meth:`PriceDataLoader.get_prices`:
    - Index: ``DatetimeIndex`` (sorted ascending, no duplicates, tz-naive)
    - Columns: ``Open``, ``High``, ``Low``, ``Close``, ``Volume``
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from trading_bot import config

REQUIRED_COLUMNS: tuple[str, ...] = ("Open", "High", "Low", "Close", "Volume")


class DataLoaderError(Exception):
    """Raised when price data can't be fetched or fails validation."""


class PriceDataLoader:
    """Download historical OHLCV data with ``yfinance`` and cache it on disk.

    Args:
        cache_dir: Folder where cached CSV/Parquet files are written.
        max_age_hours: Cached files older than this are treated as stale.
    """

    def __init__(
        self,
        cache_dir: Path = config.CACHE_DIR,
        max_age_hours: int = config.CACHE_MAX_AGE_HOURS,
    ) -> None:
        # TODO: Store cache_dir and max_age_hours on self.
        # TODO: Create cache_dir if it doesn't exist (mkdir parents=True, exist_ok=True).
        pass

    def get_prices(
        self,
        ticker: str,
        period: str = config.DEFAULT_PERIOD,
        interval: str = config.DEFAULT_INTERVAL,
        use_cache: bool = True,
    ) -> pd.DataFrame:
        """Return cleaned historical prices for ``ticker``. This is the main public method.

        Uses the cache when it is fresh, otherwise downloads and refreshes it.

        Args:
            ticker: Symbol like ``"AAPL"``. Should be normalized to upper case.
            period: yfinance period string (``"1y"``, ``"5y"``, ``"max"``...).
            interval: yfinance bar size (``"1d"``, ``"1wk"``...).
            use_cache: If False, always download fresh data.

        Returns:
            A validated OHLCV DataFrame (see module docstring).

        Raises:
            DataLoaderError: If no data comes back or validation fails.
        """
        # TODO: Normalize ticker (strip + upper).
        # TODO: Build the cache path with self._cache_path(...).
        # TODO: If use_cache and self._is_cache_fresh(path): return self.load_cache(path).
        # TODO: Otherwise df = self.fetch(...), then df = self._clean(df).
        # TODO: self._validate(df), self.save_cache(df, path), return df.
        raise NotImplementedError

    def fetch(self, ticker: str, period: str, interval: str) -> pd.DataFrame:
        """Download raw data from Yahoo Finance with ``yfinance``.

        Args:
            ticker: Upper-case symbol.
            period: yfinance period string.
            interval: yfinance interval string.

        Returns:
            The raw DataFrame from yfinance (not yet cleaned).

        Raises:
            DataLoaderError: If yfinance returns an empty DataFrame
                (bad ticker, delisted, or network problem).
        """
        # TODO: import yfinance as yf (import inside here keeps tests offline-friendly).
        # TODO: df = yf.Ticker(ticker).history(period=period, interval=interval, auto_adjust=True)
        #       (or yf.download(...); note that yf.download may return MultiIndex columns).
        # TODO: If df.empty, raise DataLoaderError with a helpful message.
        # TODO: Return df.
        raise NotImplementedError

    def load_cache(self, path: Path) -> pd.DataFrame:
        """Read a cached price file from disk.

        Args:
            path: File produced by :meth:`save_cache`.

        Returns:
            DataFrame with a parsed DatetimeIndex.
        """
        # TODO: pd.read_csv(path, index_col=0, parse_dates=True) (or read_parquet).
        # TODO: Return the DataFrame.
        raise NotImplementedError

    def save_cache(self, df: pd.DataFrame, path: Path) -> None:
        """Write a price DataFrame to the cache.

        Args:
            df: Cleaned OHLCV data.
            path: Destination file.
        """
        # TODO: df.to_csv(path) (or to_parquet if you add pyarrow).
        pass

    def _cache_path(self, ticker: str, period: str, interval: str) -> Path:
        """Build a deterministic cache filename, e.g. ``AAPL_2y_1d.csv``."""
        # TODO: Return self.cache_dir / f"{ticker}_{period}_{interval}.csv".
        raise NotImplementedError

    def _is_cache_fresh(self, path: Path) -> bool:
        """Return True if ``path`` exists and is younger than ``max_age_hours``."""
        # TODO: If not path.exists(): return False.
        # TODO: Compare path.stat().st_mtime to time.time(); age in hours <= max_age_hours.
        raise NotImplementedError

    @staticmethod
    def _clean(df: pd.DataFrame) -> pd.DataFrame:
        """Normalize raw yfinance output into the standard shape.

        Steps:
            - Flatten MultiIndex columns if present.
            - Keep only REQUIRED_COLUMNS.
            - Strip timezone from the index (tz_localize(None)).
            - Sort by date, drop duplicate dates, drop rows where Close is NaN.
        """
        # TODO: Implement the steps listed in the docstring.
        raise NotImplementedError

    @staticmethod
    def _validate(df: pd.DataFrame) -> None:
        """Raise :class:`DataLoaderError` if ``df`` isn't usable.

        Checks:
            - Not empty.
            - All REQUIRED_COLUMNS present.
            - Index is a DatetimeIndex and is monotonic increasing.
        """
        # TODO: Implement each check and raise DataLoaderError with a clear message.
        pass
