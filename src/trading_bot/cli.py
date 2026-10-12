"""Command-line interface.

Example usage (once implemented):
    python main.py AAPL
    python main.py AAPL MSFT --strategy ma --short 20 --long 50
    python main.py AAPL --backtest --period 5y
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from trading_bot import config
from trading_bot.strategies import STRATEGIES, Strategy


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser.

    Arguments to add:
        tickers (positional, nargs="+"): one or more symbols.
        --strategy: choice from STRATEGIES keys, default "ma".
        --short: int, default config.DEFAULT_SHORT_WINDOW.
        --long: int, default config.DEFAULT_LONG_WINDOW.
        --period: yfinance period, default config.DEFAULT_PERIOD.
        --backtest: flag; also run a backtest and print its summary.
        --no-cache: flag; force a fresh download.
    """
    # TODO: Build and return the parser described above.
    raise NotImplementedError


def build_strategy(args: argparse.Namespace) -> Strategy:
    """Instantiate the strategy chosen on the command line.

    Args:
        args: Parsed arguments.

    Returns:
        A configured :class:`Strategy`, e.g.
        ``MovingAverageCrossover(args.short, args.long)``.
    """
    # TODO: Look up STRATEGIES[args.strategy] and pass the relevant params.
    raise NotImplementedError


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point.

    Steps:
        1. Parse args (argv=None means use sys.argv).
        2. Build the strategy and a PriceDataLoader.
        3. For each ticker:
             a. generate_suggestion(...) and print suggestion.format()
             b. If --backtest, run Backtester().run(...) and print result.summary()
             c. Catch DataLoaderError / ValueError per ticker, print a friendly
                error, and continue with the next ticker.
        4. Return 0 if every ticker succeeded, 1 otherwise.

    Args:
        argv: Argument list, mainly for tests.

    Returns:
        Process exit code.
    """
    # TODO: Implement steps 1-4.
    raise NotImplementedError
