"""Вправа 2: Виправити mutable default. Запуск: pytest exercise_2_mutable_fix.py -v"""


def collect_errors(error, errors=None):
    """Зібрати помилки — кожен виклик має свій список."""
    # TODO: замініть pass на:
    #   if errors is None:
    #       errors = []
    #   errors.append(error)
    #   return errors
    pass

def create_response(status, data=None, headers=None):
    """Створити response — кожен має свої data та headers."""
    # TODO: замініть pass на:
    #   if data is None:
    #       data = {}
    #   if headers is None:
    #       headers = {}
    #   return {"status": status, "data": data, "headers": headers}
    pass

def test_collect_independent():
    # TODO: замініть pass на:
    #   r1 = collect_errors("timeout")
    #   r2 = collect_errors("404")
    #   assert r1 == ["timeout"]
    #   assert r2 == ["404"]
    pass

def test_response_independent():
    # TODO: замініть pass на:
    #   r1 = create_response(200)
    #   r2 = create_response(201)
    #   r1["data"]["key"] = "value"
    #   assert r2["data"] == {}
    pass