"""Приклад 3: абстракція. Запуск: pytest example_3_abstraction.py -v"""

from abc import ABC, abstractmethod


class EmailSender:
    """Простий інтерфейс send(), деталі сховані."""
    def send(self, to, text):
        self._connect()
        self._authenticate()
        return f"Sent '{text}' to {to}"

    def _connect(self):
        return "connected"

    def _authenticate(self):
        return "authenticated"


class ApiClient:
    """Ховає токен та деталі HTTP за простими методами."""
    def __init__(self, token):
        self.__token = token

    def get_user(self, user_id):
        return {"id": user_id, "auth": bool(self.__token)}


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2


def test_email_simple_interface():
    sender = EmailSender()
    result = sender.send("qa@test.com", "hello")
    assert result == "Sent 'hello' to qa@test.com"

def test_api_client_hides_token():
    client = ApiClient("secret-token")
    user = client.get_user(7)
    assert user == {"id": 7, "auth": True}
    # токен схований (name mangling)
    assert client._ApiClient__token == "secret-token"

def test_abstract_cannot_instantiate():
    import pytest
    with pytest.raises(TypeError):
        Shape()

def test_concrete_subclass_works():
    c = Circle(10)
    assert c.area() == 314.0
