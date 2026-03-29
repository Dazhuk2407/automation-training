"""
Вправа 1: Positional та keyword аргументи.
Запуск: pytest exercise_1_positional.py -v
"""


def create_user(name, role):
    return {"name": name, "role": role}


def test_positional():
    # TODO: замініть pass на:
    #   user = create_user("Alice", "admin")
    #   assert user["name"] == "Alice"
    #   assert user["role"] == "admin"
    pass

def test_keyword():
    # TODO: замініть pass на:
    #   user = create_user(name="Bob", role="user")
    #   assert user["name"] == "Bob"
    pass

def test_reversed_keyword():
    # TODO: замініть pass на:
    #   user = create_user(role="admin", name="Charlie")
    #   assert user["name"] == "Charlie"
    #   assert user["role"] == "admin"
    pass