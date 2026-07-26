"""Приклад 3: ланцюг викликів у traceback. Запуск: pytest example_3_nested_calls.py -v"""
import traceback


def level_c(a, b):
    return a / b  # 💥 реальне місце помилки


def level_b(a, b):
    return level_c(a, b)


def level_a(a, b):
    return level_b(a, b)


def capture_stack():
    """A → B → C: захопити traceback усього ланцюга."""
    try:
        return level_a(10, 0)
    except ZeroDivisionError:
        return traceback.format_exc()


def test_stack_contains_all_frames():
    tb = capture_stack()
    # traceback показує весь ланцюг викликів
    assert "level_a" in tb
    assert "level_b" in tb
    assert "level_c" in tb


def test_real_error_is_in_level_c():
    tb = capture_stack()
    lines = tb.splitlines()
    # знаходимо рядок з реальним виразом, що впав
    boom_index = next(i for i, ln in enumerate(lines) if "return a / b" in ln)
    # у попередньому рядку — функція level_c (де впало насправді)
    assert "level_c" in lines[boom_index - 1]


def test_last_line_is_the_diagnosis():
    tb = capture_stack()
    assert tb.strip().splitlines()[-1] == "ZeroDivisionError: division by zero"
