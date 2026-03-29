"""
Вправа 2: Валідація з early return.
Запуск: pytest exercise_2_validate.py -v
"""


def validate_password(pwd):
    """Валідація пароля: empty / too_short / no_digit / valid."""
    # TODO: замініть pass на:
    #   if not pwd:
    #       return "empty"
    #   if len(pwd) < 8:
    #       return "too_short"
    #   if not any(c.isdigit() for c in pwd):
    #       return "no_digit"
    #   return "valid"
    pass


def validate_config(config):
    """Валідація конфігурації: missing_host / missing_port / valid."""
    # TODO: замініть pass на:
    #   if "host" not in config:
    #       return "missing_host"
    #   if "port" not in config:
    #       return "missing_port"
    #   return "valid"
    pass


def test_password_valid():
    # TODO: замініть pass на: assert validate_password("MyPass123") == "valid"
    pass

def test_password_empty():
    # TODO: замініть pass на: assert validate_password("") == "empty"
    pass

def test_password_short():
    # TODO: замініть pass на: assert validate_password("Ab1") == "too_short"
    pass

def test_password_no_digit():
    # TODO: замініть pass на: assert validate_password("LongPassword") == "no_digit"
    pass

def test_config_valid():
    # TODO: замініть pass на: assert validate_config({"host": "localhost", "port": 8080}) == "valid"
    pass

def test_config_missing_host():
    # TODO: замініть pass на: assert validate_config({"port": 8080}) == "missing_host"
    pass