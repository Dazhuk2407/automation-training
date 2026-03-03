"""
Приклад скрипта з аргументами командного рядка.

Цей скрипт демонструє:
- Робота з sys.argv
- Отримання аргументів з командного рядка
- Умовна логіка
"""

import sys


def main() -> None:
    if len(sys.argv) > 1:
        print(f"Hello, {sys.argv[1]}!")
    else:
        print("Hello, World!")


if __name__ == "__main__":
    main()

