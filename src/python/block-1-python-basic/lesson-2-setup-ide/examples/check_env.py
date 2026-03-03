"""
Приклад перевірки налаштувань Python оточення.

Цей скрипт показує:
- Версію Python
- Шлях до інтерпретатора
- Поточну робочу директорію
"""

import sys
import os


def main() -> None:
    print(f"Python: {sys.version}")
    print(f"Interpreter: {sys.executable}")
    print(f"Path: {os.getcwd()}")


if __name__ == "__main__":
    main()

