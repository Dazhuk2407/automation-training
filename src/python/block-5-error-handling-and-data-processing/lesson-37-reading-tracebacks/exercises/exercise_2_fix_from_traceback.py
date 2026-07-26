"""Вправа 2: виправ за traceback. Запуск: pytest exercise_2_fix_from_traceback.py -v

Один з тестів падає. Запусти тести, прочитай traceback ЗНИЗУ ВГОРУ:
  1. останній рядок = тип винятку + повідомлення;
  2. рядок 'File ... line ... in <функція>' = де саме впало у твоєму коді.
Знайди функцію з коментарем '# BUG:' і виправ її. Після фіксу — все зелено.
"""


def get_first(items):
    return items[0]


def get_last(items):
    # BUG: IndexError — індекс len(items) виходить за межі (треба len(items) - 1)
    return items[len(items)]


def get_middle(items):
    return items[len(items) // 2]


def test_first():
    assert get_first([10, 20, 30]) == 10


def test_first_single():
    assert get_first([99]) == 99


def test_middle():
    assert get_middle([1, 2, 3]) == 2


def test_last():
    # цей тест падає, поки get_last не виправлено — читай traceback
    assert get_last([10, 20, 30]) == 30
