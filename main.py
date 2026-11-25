"""Terrible-advice dispatcher for Worst AI Advice."""
import os
from pathlib import Path

CONFIG = {
    "input": "entry.txt",
    "ceiling": 140,
}
NOTE = "worst advice only"


def run():
    home = Path(__file__).resolve().parent
    src = home / CONFIG["input"]
    data = src.read_bytes()
    text = data.decode("utf-8").strip()
    size = len(text)
    if size == 0:
        raise SystemExit("advice empty")
    elif size > CONFIG["ceiling"]:
        raise SystemExit(f"advice over ceiling: {size}")
    else:
        dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "entry.txt").write_bytes(text.encode("utf-8"))
        print("ADVICE_DISPATCHED", size, "chars", "|", NOTE)


if __name__ == "__main__":
    run()
