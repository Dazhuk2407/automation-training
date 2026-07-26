"""Модуль-приклад: прості утиліти. Це НЕ тестовий файл, його імпортують."""


def greet(name):
    return f"Hello, {name}"


def double(x):
    return x * 2


if __name__ == "__main__":
    # Виконається лише при `python helpers.py`, не при import
    print(greet("World"))
    print(double(21))
