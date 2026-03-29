"""
Вправа 3: break + continue + else.
Запуск: pytest exercise_3_combined.py -v
"""


def test_skip_and_stop():
    """continue для None, break для 'STOP'."""
    commands = ["run", None, "check", "STOP", "clean"]
    # TODO: замініть pass на:
    #   executed = []
    #   for cmd in commands:
    #       if cmd is None:
    #           continue
    #       if cmd == "STOP":
    #           break
    #       executed.append(cmd)
    #   assert executed == ["run", "check"]
    pass


def test_else_all_ok():
    """else виконується коли break не спрацював."""
    codes = [200, 201, 204]
    # TODO: замініть pass на:
    #   all_ok = False
    #   for code in codes:
    #       if code >= 400:
    #           break
    #   else:
    #       all_ok = True
    #   assert all_ok is True
    pass


def test_else_has_error():
    """else НЕ виконується після break."""
    codes = [200, 404, 500]
    # TODO: замініть pass на:
    #   all_ok = False
    #   for code in codes:
    #       if code >= 400:
    #           break
    #   else:
    #       all_ok = True
    #   assert all_ok is False
    pass