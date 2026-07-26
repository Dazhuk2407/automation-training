"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_static.py -v

Тести падають — знайди рядок з коментарем `# BUG:` та виправ його.
Рівно один тест падає до виправлення.
"""


class Validator:
    @staticmethod
    def is_valid_status_code(code):
        # BUG: діапазон невірний — 2xx це 200..299, а не 200..399
        return 200 <= code < 400

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


class TestId:
    @staticmethod
    def generate(prefix, number):
        return f"{prefix}-{number:04d}"


def test_valid_status_ok():
    assert Validator.is_valid_status_code(200) is True

def test_redirect_is_not_success():
    # 301 (redirect) не є успішним 2xx кодом
    assert Validator.is_valid_status_code(301) is False

def test_valid_email():
    assert Validator.is_valid_email("qa@example.com") is True

def test_generate_id():
    assert TestId.generate("TC", 42) == "TC-0042"
