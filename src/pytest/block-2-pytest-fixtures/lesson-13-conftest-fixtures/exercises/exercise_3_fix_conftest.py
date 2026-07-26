"""
Вправа 3: Виправ conftest-фікстуру.

Тут один тест навмисно падає. Фікстура sample_user приходить з
exercises/conftest.py і має role == "admin", але тест очікує інше.

Крок 1: Запустіть файл — один тест падає.
Крок 2: Прочитайте вивід pytest — яке значення насправді у фікстурі?
Крок 3: Виправте очікуване значення у тесті.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_conftest.py -v
"""


def test_user_role_is_admin(sample_user):
    """Цей тест падає — фікстура з conftest дає інший role."""
    # TODO: sample_user["role"] насправді дорівнює "admin", не "user" — виправте
    assert sample_user["role"] == "user"


def test_user_name(sample_user):
    """Цей тест уже коректний."""
    assert sample_user["name"] == "Alice"


def test_config_timeout(app_config):
    """Цей тест уже коректний."""
    assert app_config["timeout"] == 5


# ВІДПОВІДЬ:
# Чому тест падав: _______________
# Яке значення role у conftest-фікстурі: _______________
# Чи треба import фікстури з conftest (так/ні): _______________
