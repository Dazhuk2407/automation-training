"""
Вправа 1: Підрахунок summary з JUnit XML.

parse_summary та passed_count уже реалізовані, SAMPLE надано.
Замініть pass на правильний assert.

Запуск: pytest exercise_1_parse.py -v
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


def test_tests_count():
    """tests має дорівнювати 4."""
    s = parse_summary(SAMPLE)
    # TODO: замініть pass на: assert s["tests"] == 4
    pass


def test_failures_count():
    """failures має дорівнювати 1."""
    s = parse_summary(SAMPLE)
    # TODO: замініть pass на: assert s["failures"] == 1
    pass


def test_skipped_count():
    """skipped має дорівнювати 1."""
    s = parse_summary(SAMPLE)
    # TODO: замініть pass на: assert s["skipped"] == 1
    pass


def test_passed_count():
    """passed = 4 - 1 - 1 = 2."""
    s = parse_summary(SAMPLE)
    # TODO: замініть pass на: assert passed_count(s) == 2
    pass


def test_root_tag():
    """Кореневий тег — testsuite."""
    root = ET.fromstring(SAMPLE)
    # TODO: замініть pass на: assert root.tag == "testsuite"
    pass
