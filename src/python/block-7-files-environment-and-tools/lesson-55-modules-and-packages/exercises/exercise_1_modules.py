"""Вправа 1: модулі. Запуск: pytest exercise_1_modules.py -v

Уяви, що ці функції — вміст твого модуля `utils`.
Реалізуй їх (прибери pass) і допиши asserts у тестах.
"""


def module_mode(name):
    # TODO: поверни "script" якщо name == "__main__", інакше "imported"
    # TODO: return "script" if name == "__main__" else "imported"
    pass


def shout(text):
    # TODO: return text.upper() + "!"
    pass


def is_blank(text):
    # TODO: return len(text.strip()) == 0
    pass


def test_mode_script():
    # TODO: assert module_mode("__main__") == "script"
    pass


def test_mode_imported():
    # TODO: assert module_mode("utils") == "imported"
    pass


def test_shout():
    # TODO: assert shout("hi") == "HI!"
    pass


def test_is_blank_true():
    # TODO: assert is_blank("   ") is True
    pass


def test_is_blank_false():
    # TODO: assert is_blank("x") is False
    pass
