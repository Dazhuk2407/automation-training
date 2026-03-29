"""Приклад 3: Return у тестових helper-функціях. Запуск: pytest example_3_in_tests.py -v"""


def parse_status(code):
    if code < 400:
        return "success", False
    return "error", True

def classify_codes(codes):
    result = {"success": 0, "error": 0}
    for code in codes:
        cat, _ = parse_status(code)
        result[cat] += 1
    return result

def find_first_error(codes):
    for code in codes:
        if code >= 400:
            return code
    return None

def test_parse_success():
    cat, err = parse_status(200)
    assert cat == "success"
    assert err is False

def test_parse_error():
    cat, err = parse_status(500)
    assert cat == "error"
    assert err is True

def test_classify():
    assert classify_codes([200, 200, 404, 500]) == {"success": 2, "error": 2}

def test_find_first_error():
    assert find_first_error([200, 200, 404, 500]) == 404

def test_find_no_error():
    assert find_first_error([200, 201]) is None