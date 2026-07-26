"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_inherit.py -v

Один з тестів падає. Знайди рядок з `# BUG:` і виправ його.
Підказка: підклас втрачає атрибут батька.
"""


class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def describe(self):
        return f"{self.owner}: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, owner, rate):
        # BUG: забутий виклик super().__init__(owner) → self.owner і self.balance зникають
        self.rate = rate

    def apply_interest(self):
        self.balance += self.balance * self.rate


def test_has_rate():
    acc = SavingsAccount("Alice", 0.1)
    assert acc.rate == 0.1

def test_has_owner():
    acc = SavingsAccount("Alice", 0.1)
    assert acc.owner == "Alice"

def test_is_account():
    acc = SavingsAccount("Alice", 0.1)
    assert isinstance(acc, Account)

def test_is_subclass():
    assert issubclass(SavingsAccount, Account)
