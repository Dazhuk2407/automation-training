"""
Приклад 2: Розбір окремих <testcase> у JUnit XML.

Дістаємо імена всіх тестів та імена лише тих, що впали (містять <failure>).
Парсимо готовий XML-рядок через xml.etree.ElementTree.

Запуск: pytest example_2_parse_report.py -v
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


def all_test_names(xml_text):
    """Імена всіх тестів у звіті (у порядку появи)."""
    root = ET.fromstring(xml_text)
    return [case.get("name") for case in root.findall("testcase")]


def failed_test_names(xml_text):
    """Імена тестів, у яких є вкладений <failure>."""
    root = ET.fromstring(xml_text)
    names = []
    for case in root.findall("testcase"):
        if case.find("failure") is not None:
            names.append(case.get("name"))
    return names


def skipped_test_names(xml_text):
    """Імена тестів, у яких є вкладений <skipped>."""
    root = ET.fromstring(xml_text)
    return [
        case.get("name")
        for case in root.findall("testcase")
        if case.find("skipped") is not None
    ]


def test_all_names():
    """Усі 4 імені в правильному порядку."""
    assert all_test_names(SAMPLE) == ["test_a", "test_b", "test_c", "test_d"]


def test_failed_names():
    """Впав лише test_b."""
    assert failed_test_names(SAMPLE) == ["test_b"]


def test_skipped_names():
    """Пропущено лише test_c."""
    assert skipped_test_names(SAMPLE) == ["test_c"]


def test_passed_are_the_rest():
    """passed = усі мінус впалі мінус пропущені."""
    passed = (
        set(all_test_names(SAMPLE))
        - set(failed_test_names(SAMPLE))
        - set(skipped_test_names(SAMPLE))
    )
    assert passed == {"test_a", "test_d"}
