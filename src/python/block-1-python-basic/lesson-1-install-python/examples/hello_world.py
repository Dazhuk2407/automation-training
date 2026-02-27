"""Simple script to verify Python is running."""

import sys
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[3]
    print("Hello from Python!")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Project root: {project_root}")


if __name__ == "__main__":
    main()

