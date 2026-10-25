#!/usr/bin/env python3
from pathlib import Path
from arxa.core import run

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    result = run(root)
    print(result)
