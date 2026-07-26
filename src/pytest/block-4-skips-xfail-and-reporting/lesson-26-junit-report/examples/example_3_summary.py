"""
Приклад 3: Побудова людино-читабельного summary-рядка.

З JUnit XML рахуємо результати і формуємо рядок виду:
"Tests: 4, Passed: 2, Failed: 1, Skipped: 1".

Запуск: pytest example_3_summary.py -v
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
    """Лічильники з кореневого <testsuite>."""
    root = ET.fromstring(xml_text)
    return {
        "tests": int(root.get("tests")),
        "failures": int(root.get("failures")),
        "skipped": int(root.get("skipped")),
    }


def passed_count(summary):
    return summary["tests"] - summary["failures"] - summary["skipped"]


def summary_line(xml_text):
    """Побудувати підсумковий рядок для звіту в CI/чаті."""
    s = parse_summary(xml_text)
    return (
        f"Tests: {s['tests']}, "
        f"Passed: {passed_count(s)}, "
        f"Failed: {s['failures']}, "
        f"Skipped: {s['skipped']}"
    )


def test_summary_line():
    """Повний підсумковий рядок."""
    assert summary_line(SAMPLE) == "Tests: 4, Passed: 2, Failed: 1, Skipped: 1"


def test_summary_starts_with_total():
    """Рядок починається із загальної кількості тестів."""
    assert summary_line(SAMPLE).startswith("Tests: 4")


def test_passed_in_line():
    """У рядку відображено правильну кількість passed."""
    assert "Passed: 2" in summary_line(SAMPLE)
