"""Trading strategies that turn price data into BUY / SELL / HOLD signals."""

from trading_bot.strategies.base import Signal, Strategy
from trading_bot.strategies.ma_crossover import MovingAverageCrossover

# Name -> class lookup used by the CLI's --strategy flag.
STRATEGIES: dict[str, type[Strategy]] = {
    "ma": MovingAverageCrossover,
}

__all__ = ["Signal", "Strategy", "MovingAverageCrossover", "STRATEGIES"]
