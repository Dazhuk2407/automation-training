"""
Вправа 2: Побудова summary-рядка з JUnit XML.

summary_line уже реалізовано, SAMPLE надано.
Замініть pass на правильний assert.

Запуск: pytest exercise_2_summary.py -v
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
    return summary["tests"] - summary["failures"] - summary["skipped"]


def summary_line(xml_text):
    s = parse_summary(xml_text)
    return (
        f"Tests: {s['tests']}, "
        f"Passed: {passed_count(s)}, "
        f"Failed: {s['failures']}, "
        f"Skipped: {s['skipped']}"
    )


def test_full_line():
    """Повний рядок summary."""
    # TODO: замініть pass на:
    # assert summary_line(SAMPLE) == "Tests: 4, Passed: 2, Failed: 1, Skipped: 1"
    pass


def test_starts_with_total():
    """Рядок починається з 'Tests: 4'."""
    # TODO: замініть pass на: assert summary_line(SAMPLE).startswith("Tests: 4")
    pass


def test_contains_passed():
    """У рядку є 'Passed: 2'."""
    # TODO: замініть pass на: assert "Passed: 2" in summary_line(SAMPLE)
    pass


def test_contains_failed():
    """У рядку є 'Failed: 1'."""
    # TODO: замініть pass на: assert "Failed: 1" in summary_line(SAMPLE)
    pass
