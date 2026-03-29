"""
Приклад 2: Тести для рядків.

Запуск: pytest example_2_strings.py -v
"""


def test_equality():
    """Рівність рядків (регістр має значення)."""
    assert "hello" == "hello"
    assert "Hello" != "hello"


def test_contains():
    """Перевірка вмісту підрядка."""
    text = "pytest testing framework"
    assert "pytest" in text
    assert "test" in text
    assert "Java" not in text


def test_starts_and_ends():
    """Початок та кінець рядка."""
    url = "https://example.com"
    assert url.startswith("https://")
    assert url.endswith(".com")
    assert not url.startswith("http://")


def test_case_methods():
    """Методи зміни регістру."""
    assert "hello".upper() == "HELLO"
    assert "WORLD".lower() == "world"
    assert "python".capitalize() == "Python"
    assert "hello world".title() == "Hello World"


def test_strip_and_split():
    """Очищення та розділення."""
    assert "  spaces  ".strip() == "spaces"
    assert "a,b,c".split(",") == ["a", "b", "c"]
    assert "Hello World".split() == ["Hello", "World"]


def test_length():
    """Довжина рядка."""
    password = "MyPassword123"
    assert len(password) >= 8
    assert len(password) <= 20
    assert len("") == 0