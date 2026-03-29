"""
Приклад 3: else у циклах та комбіновані паттерни.
Запуск: pytest example_3_else_and_patterns.py -v
"""


def test_else_when_no_break():
    """else виконується коли break не спрацював."""
    codes = [200, 201, 204]
    all_ok = False
    for code in codes:
        if code >= 400:
            break
    else:
        all_ok = True
    assert all_ok is True


def test_else_when_break():
    """else НЕ виконується коли break спрацював."""
    codes = [200, 404, 500]
    all_ok = False
    for code in codes:
        if code >= 400:
            break
    else:
        all_ok = True
    assert all_ok is False


def test_else_empty_loop():
    """else виконується навіть для порожнього циклу."""
    executed = False
    for item in []:
        pass
    else:
        executed = True
    assert executed is True


def test_combined_break_continue():
    """Пропустити None, зупинитися на 'STOP'."""
    commands = ["run", None, "check", "STOP", "clean"]
    executed = []
    for cmd in commands:
        if cmd is None:
            continue
        if cmd == "STOP":
            break
        executed.append(cmd)
    assert executed == ["run", "check"]