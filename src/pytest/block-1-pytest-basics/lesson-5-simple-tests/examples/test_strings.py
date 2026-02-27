"""Lesson 5: Example 2 - Testing Strings"""
def test_string_equality():
    assert "hello" == "hello"
    assert "Hello" != "hello"
def test_string_methods():
    text = "Python Testing"
    assert text.upper() == "PYTHON TESTING"
    assert text.lower() == "python testing"
    assert text.split() == ["Python", "Testing"]
def test_string_contains():
    assert "test" in "pytest"
    assert "java" not in "pytest"
def test_string_startswith_endswith():
    url = "https://example.com"
    assert url.startswith("https://")
    assert url.endswith(".com")
