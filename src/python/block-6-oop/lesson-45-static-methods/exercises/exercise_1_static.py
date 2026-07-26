"""Вправа 1: @staticmethod. Запуск: pytest exercise_1_static.py -v"""


class Validator:
    @staticmethod
    def is_valid_email(email):
        # TODO: return "@" in email and "." in email
        pass

    @staticmethod
    def is_valid_status_code(code):
        # TODO: return 200 <= code < 300
        pass


class TestId:
    @staticmethod
    def generate(prefix, number):
        # TODO: return f"{prefix}-{number:04d}"
        pass


def test_valid_email():
    # TODO: assert Validator.is_valid_email("qa@example.com") is True
    pass

def test_invalid_email():
    # TODO: assert Validator.is_valid_email("broken") is False
    pass

def test_valid_status():
    # TODO: assert Validator.is_valid_status_code(200) is True
    pass

def test_invalid_status():
    # TODO: assert Validator.is_valid_status_code(500) is False
    pass

def test_generate_id():
    # TODO: assert TestId.generate("TC", 7) == "TC-0007"
    pass
