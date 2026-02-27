#!/bin/bash
# Example: Check pytest installation

echo "=== Checking Python version ==="
python --version

echo ""
echo "=== Checking pytest version ==="
pytest --version

echo ""
echo "=== Checking pip list for pytest ==="
pip list | grep pytest

echo ""
echo "=== Pytest is ready! ==="

