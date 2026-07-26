"""
Реєстрація власних маркерів для прикладів Lesson 17.

У кореневому pytest.ini увімкнено --strict-markers, тому будь-який
незареєстрований маркер спричинить помилку. Маркери smoke/regression/slow
вже зареєстровані глобально — тут реєструємо лише власні.
"""


def pytest_configure(config):
    config.addinivalue_line("markers", "api: тести API-рівня")
    config.addinivalue_line("markers", "ui: тести UI-рівня")
    config.addinivalue_line("markers", "critical: критичні перевірки")
