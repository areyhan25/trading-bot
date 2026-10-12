"""Tests for trading_bot.cli."""

import pytest

from trading_bot.cli import build_parser, main  # noqa: F401


@pytest.mark.skip(reason="TODO: implement the CLI first")
def test_parser_defaults():
    # TODO: args = build_parser().parse_args(["AAPL"]); assert args.strategy == "ma".
    # TODO: Also test: main([...]) returns 1 when a ticker fails
    #       (monkeypatch generate_suggestion to raise).
    pass
