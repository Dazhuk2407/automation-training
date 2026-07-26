"""
Реєстрація власних маркерів для вправ Lesson 17.

У кореневому pytest.ini увімкнено --strict-markers. Маркери smoke/regression/slow
вже зареєстровані глобально — тут реєструємо лише власні, які потрібні у вправах.
"""


def pytest_configure(config):
    config.addinivalue_line("markers", "api: тести API-рівня")
    config.addinivalue_line("markers", "ui: тести UI-рівня")
    config.addinivalue_line("markers", "critical: критичні перевірки")
