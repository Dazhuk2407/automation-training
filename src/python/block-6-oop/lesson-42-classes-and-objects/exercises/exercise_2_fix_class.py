"""Вправа 2: Виправ помилку. Запуск: pytest exercise_2_fix_class.py -v

Деякі тести падають. Знайди рядок з `# BUG:` і виправ його,
щоб усі тести проходили.
"""

import pytest


class BankAccount:
    def open(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def get_balance(self):
        # BUG: повертає не той атрибут (owner замість balance)
        return self.owner


def test_open():
    acc = BankAccount()
    acc.open("Alice")
    assert acc.owner == "Alice"
    assert acc.balance == 0

def test_deposit():
    acc = BankAccount()
    acc.open("Alice")
    acc.deposit(100)
    assert acc.balance == 100

def test_withdraw():
    acc = BankAccount()
    acc.open("Alice")
    acc.deposit(100)
    acc.withdraw(30)
    assert acc.get_balance() == 70

def test_withdraw_too_much():
    acc = BankAccount()
    acc.open("Alice")
    acc.deposit(50)
    with pytest.raises(ValueError) as exc_info:
        acc.withdraw(100)
    assert "insufficient" in str(exc_info.value)
