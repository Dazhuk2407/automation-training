# Приклади — Lesson 20: Test Suites

У цій папці — приклади організації тестів у набори (smoke / regression).

## Файли

- `conftest.py` — реєструє власний маркер `critical` (smoke/regression/slow вже глобальні)
- `example_1_smoke_suite.py` — smoke-набір: невелика підмножина критичних тестів
- `example_2_regression_suite.py` — regression-набір: повне покриття, smoke ⊂ regression
- `example_3_organize.py` — класифікація тестів у набори як чиста функція (`suite_of`, `count_suites`)

## Як запускати

```bash
# усі приклади
pytest -v

# тільки smoke-набір
pytest -m smoke -v

# тільки regression-набір (включає критичні smoke-тести)
pytest -m regression -v

# усе, крім повільних
pytest -m "not slow" -v
```

Усі тести в цій папці **проходять** — вони демонструють коректну організацію наборів.
