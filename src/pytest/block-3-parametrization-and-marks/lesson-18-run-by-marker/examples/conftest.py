"""
Локальна реєстрація маркерів для прикладів Lesson 18.

Маркери smoke / regression / slow вже зареєстровані глобально у pytest.ini,
але ми дублюємо реєстрацію тут, щоб приклади були самодостатніми
і працювали навіть у відриві від кореневого pytest.ini.
"""


def pytest_configure(config):
    """Register custom markers used in the examples."""
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "regression: regression tests")
    config.addinivalue_line("markers", "slow: slow running tests")
