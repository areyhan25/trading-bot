"""Entry point: ``python main.py AAPL``.

Thin wrapper around :func:`trading_bot.cli.main` so the project runs without
installing the package. Prints suggestions only; it never places trades.
"""

import sys
from pathlib import Path

# Make src/ importable when running from a fresh checkout (no `pip install -e .`).
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from trading_bot.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
