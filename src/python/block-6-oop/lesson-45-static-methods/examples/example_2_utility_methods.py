"""Приклад 2: static-утиліти для QA. Запуск: pytest example_2_utility_methods.py -v"""


class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @staticmethod
    def is_valid_status_code(code):
        return 200 <= code < 300


class TestId:
    @staticmethod
    def generate(prefix, number):
        return f"{prefix}-{number:04d}"


class Converter:
    @staticmethod
    def to_cents(dollars):
        return int(round(dollars * 100))


def test_is_valid_email():
    assert Validator.is_valid_email("qa@example.com") is True
    assert Validator.is_valid_email("broken-email") is False

def test_is_valid_status_code():
    assert Validator.is_valid_status_code(200) is True
    assert Validator.is_valid_status_code(404) is False

def test_generate_id():
    assert TestId.generate("TC", 7) == "TC-0007"
    assert TestId.generate("BUG", 123) == "BUG-0123"

def test_to_cents():
    assert Converter.to_cents(1.5) == 150
    assert Converter.to_cents(0) == 0
