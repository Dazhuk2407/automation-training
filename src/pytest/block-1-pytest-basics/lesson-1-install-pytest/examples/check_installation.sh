#!/bin/bash
# Перевірка встановлення pytest
# Запуск: bash check_installation.sh

echo "=== Python ==="
python --version 2>/dev/null || python3 --version

echo ""
echo "=== Pytest ==="
pytest --version 2>/dev/null || echo "pytest не встановлений!"

echo ""
echo "=== Встановлені пакети (pytest) ==="
python -m pip list 2>/dev/null | grep -i pytest || echo "pytest не знайдено в pip list"

echo ""
echo "=== Шлях до Python ==="
which python 2>/dev/null || which python3