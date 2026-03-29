#!/bin/bash
# Демонстрація pytest --collect-only
# Запуск: bash example_4_collect_only.sh

echo "=== Приклад 1: Правильні назви ==="
echo "pytest --collect-only example_1_correct_naming.py"
echo ""
pytest --collect-only example_1_correct_naming.py 2>/dev/null
echo ""

echo "=== Приклад 2: Класи ==="
echo "pytest --collect-only example_2_test_classes.py"
echo ""
pytest --collect-only example_2_test_classes.py 2>/dev/null
echo ""

echo "=== Приклад 3: Невидимі тести ==="
echo "pytest --collect-only example_3_invisible_tests.py"
echo ""
pytest --collect-only example_3_invisible_tests.py 2>/dev/null
echo ""

echo "=== Всі приклади разом ==="
echo "pytest --collect-only"
echo ""
pytest --collect-only 2>/dev/null