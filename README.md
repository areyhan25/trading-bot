# trading-bot

A Python tool that reads **historical** Yahoo Finance price data (via
[`yfinance`](https://github.com/ranaroussi/yfinance)), runs simple rules-based
strategies, and prints **BUY / SELL / HOLD suggestions** for a ticker. It can
also backtest a strategy on past data and report basic performance stats.

**What it does NOT do:** it never connects to a brokerage, never uses live or
streaming data, and never places trades. Its only output is text in your terminal.

> ⚠️ **Not financial advice.** This is a personal learning project. Suggestions
> come from simple historical rules, and past performance does not predict future
> results. Don't make real investment decisions based on its output.

## Project layout

```
trading-bot/
├── main.py                     # entry point: python main.py AAPL
├── requirements.txt
├── pyproject.toml              # package metadata + pytest config
├── data/cache/                 # cached downloads (gitignored)
├── notebooks/                  # exploratory scripts
├── src/trading_bot/
│   ├── config.py               # defaults (paths, windows, thresholds)
│   ├── data_loader.py          # fetch + cache OHLCV data with yfinance
│   ├── indicators.py           # sma, ema, rsi
│   ├── strategies/
│   │   ├── base.py             # Signal enum + Strategy ABC
│   │   └── ma_crossover.py     # moving-average crossover strategy
│   ├── backtester.py           # simulate a strategy, compute stats
│   ├── suggestion.py           # latest signal -> Suggestion
│   └── cli.py                  # argparse CLI
└── tests/                      # pytest, offline, synthetic data
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage (once implemented)

```bash
python main.py AAPL
python main.py AAPL MSFT --short 20 --long 50
python main.py AAPL --backtest --period 5y
```

## Running tests

```bash
pytest
```

All tests start out **skipped**. Remove the `@pytest.mark.skip` from a test once
you've implemented the code it covers.

## Roadmap

This repo is a skeleton: every function body is a `TODO`. Suggested order:

### 1. Indicators (no network needed, good warm-up)
- [ ] `sma()`
- [ ] `ema()`
- [ ] `rsi()` (Wilder's smoothing, handle zero-loss case)
- [ ] Un-skip and flesh out `tests/test_indicators.py`

### 2. Data loader
- [ ] `PriceDataLoader.__init__` (create cache dir)
- [ ] `fetch()` with yfinance, raise on empty data
- [ ] `_clean()` and `_validate()`
- [ ] `_cache_path()`, `_is_cache_fresh()`, `save_cache()`, `load_cache()`
- [ ] `get_prices()` tying it all together
- [ ] Un-skip `tests/test_data_loader.py` (monkeypatch `fetch`, no real network)

### 3. Strategy
- [ ] `Strategy.latest_signal()` and `describe()`
- [ ] `MovingAverageCrossover`: validation, `generate_signals()`, `min_history()`, `describe()`
- [ ] Un-skip `tests/test_strategies.py`

### 4. Backtester
- [ ] `total_return`, `buy_and_hold_return`, `max_drawdown`, `win_rate`
- [ ] `Trade.return_pct`
- [ ] `Backtester.run()` (next-bar-open execution, long-only)
- [ ] `BacktestResult.summary()`
- [ ] Un-skip `tests/test_backtester.py`

### 5. Suggestion + CLI
- [ ] `explain_signal()`, `generate_suggestion()`, `Suggestion.format()`
- [ ] `build_parser()`, `build_strategy()`, `main()`
- [ ] Un-skip `tests/test_suggestion.py` and `tests/test_cli.py`
- [ ] End-to-end: `python main.py AAPL --backtest` works

### Stretch ideas
- [ ] RSI mean-reversion strategy (BUY < 30, SELL > 70)
- [ ] Commission/slippage in the backtester
- [ ] Sharpe ratio and annualized return
- [ ] Plot equity curve vs. buy-and-hold with matplotlib
- [ ] Compare multiple strategies side by side
