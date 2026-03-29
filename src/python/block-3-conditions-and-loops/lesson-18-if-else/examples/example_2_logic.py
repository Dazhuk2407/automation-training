"""
Приклад 2: Логічні оператори та early return.

Запуск: pytest example_2_logic.py -v
"""


def can_access(user):
    """Перевірити доступ: активний admin."""
    if user.get("active") and user.get("role") == "admin":
        return True
    return False


def validate_email(email):
    """Валідація email через early return."""
    if not email:
        return "empty"
    if "@" not in email:
        return "missing_at"
    if "." not in email.split("@")[1]:
        return "missing_domain"
    return "valid"


def test_access_granted():
    admin = {"name": "Alice", "role": "admin", "active": True}
    assert can_access(admin) is True


def test_access_denied_inactive():
    inactive = {"name": "Bob", "role": "admin", "active": False}
    assert can_access(inactive) is False


def test_access_denied_not_admin():
    user = {"name": "Charlie", "role": "user", "active": True}
    assert can_access(user) is False


def test_email_valid():
    assert validate_email("alice@test.com") == "valid"


def test_email_empty():
    assert validate_email("") == "empty"


def test_email_no_at():
    assert validate_email("alice.test.com") == "missing_at"


def test_email_no_domain():
    assert validate_email("alice@") == "missing_domain"