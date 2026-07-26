"""
Реєстрація власних маркерів для прикладів Lesson 20.

У кореневому pytest.ini увімкнено --strict-markers, тому будь-який
незареєстрований маркер спричинить помилку. Маркери smoke/regression/slow
вже зареєстровані глобально — тут реєструємо лише власний маркер critical.
"""


def pytest_configure(config):
    config.addinivalue_line("markers", "critical: критичні перевірки")
