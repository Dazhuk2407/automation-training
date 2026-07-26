"""
Приклад 1: Структура JUnit XML і підрахунок summary.

Ми НЕ запускаємо pytest --junitxml реально. Замість цього парсимо
готовий JUnit-XML рядок через стандартний парсер xml.etree.ElementTree.

Запуск: pytest example_1_junit_format.py -v
"""

import xml.etree.ElementTree as ET


# Готовий JUnit XML: 4 тести, 1 впав (failure), 1 пропущено (skipped).
SAMPLE = (
    '<testsuite name="pytest" tests="4" failures="1" skipped="1">'
    '<testcase name="test_a"/>'
    '<testcase name="test_b"><failure message="err"/></testcase>'
    '<testcase name="test_c"><skipped/></testcase>'
    '<testcase name="test_d"/>'
    '</testsuite>'
)


def parse_summary(xml_text):
    """Прочитати лічильники з кореневого <testsuite>."""
    root = ET.fromstring(xml_text)
    return {
        "tests": int(root.get("tests")),
        "failures": int(root.get("failures")),
        "skipped": int(root.get("skipped")),
    }


def passed_count(summary):
    """passed рахується формулою — окремого атрибута в XML немає."""
    return summary["tests"] - summary["failures"] - summary["skipped"]


def test_parse_summary():
    """Атрибути <testsuite> читаються коректно."""
    s = parse_summary(SAMPLE)
    assert s["tests"] == 4
    assert s["failures"] == 1
    assert s["skipped"] == 1


def test_passed_count():
    """passed = tests - failures - skipped = 4 - 1 - 1 = 2."""
    assert passed_count(parse_summary(SAMPLE)) == 2


def test_root_tag():
    """Кореневий елемент — testsuite."""
    root = ET.fromstring(SAMPLE)
    assert root.tag == "testsuite"


def test_testcase_count():
    """Усередині рівно 4 елементи <testcase>."""
    root = ET.fromstring(SAMPLE)
    assert len(root.findall("testcase")) == 4
