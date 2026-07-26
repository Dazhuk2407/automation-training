"""
Вправа 3: Знайти і виправити помилку в підрахунку passed.

У функції passed_count є баг — вона віднімає не той атрибут.
Через це test_passed_count падає.

Крок 1: Запустіть файл — один тест падає.
Крок 2: Прочитайте вивід: яке значення отримали замість 2?
Крок 3: Виправте passed_count.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_report.py -v
"""

import xml.etree.ElementTree as ET


SAMPLE = (
    '<testsuite name="pytest" tests="4" failures="1" skipped="1">'
    '<testcase name="test_a"/>'
    '<testcase name="test_b"><failure message="err"/></testcase>'
    '<testcase name="test_c"><skipped/></testcase>'
    '<testcase name="test_d"/>'
    '</testsuite>'
)


def parse_summary(xml_text):
    root = ET.fromstring(xml_text)
    return {
        "tests": int(root.get("tests")),
        "failures": int(root.get("failures")),
        "skipped": int(root.get("skipped")),
    }


def passed_count(summary):
    # ❌ БАГ: skipped не віднімається, тому passed завищений
    return summary["tests"] - summary["failures"]


def test_tests_count():
    """Цей тест проходить."""
    assert parse_summary(SAMPLE)["tests"] == 4


def test_failures_count():
    """Цей тест проходить."""
    assert parse_summary(SAMPLE)["failures"] == 1


def test_passed_count():
    """Цей тест падає через баг у passed_count. passed = 4 - 1 - 1 = 2."""
    assert passed_count(parse_summary(SAMPLE)) == 2


# ВІДПОВІДЬ:
# passed_count повертав: _______________ замість 2
# Помилка була в: _______________
# Правильна формула: passed = tests - failures - skipped
