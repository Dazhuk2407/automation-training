# Приклади — Lesson 13: conftest.py

У цій папці показано, як спільні фікстури живуть у `conftest.py` і
використовуються тестами **без import**.

## Файли

- `conftest.py` — спільні фікстури (`sample_user`, `app_config`, `client`)
- `example_1_shared_fixture.py` — одна спільна фікстура з conftest
- `example_2_multiple_shared.py` — кілька conftest-фікстур в одному тесті
- `example_3_override.py` — локальна фікстура перекриває conftest-версію

## Як запустити

```bash
pytest example_1_shared_fixture.py -v
pytest example_2_multiple_shared.py -v
pytest example_3_override.py -v
```

Зверніть увагу: у жодному example-файлі немає `from conftest import ...`.
Pytest автоматично підхоплює `conftest.py` у цій теці.
