# Приклади — Lesson 25: Stop on First Failure

Реальний `pytest -x` / `--maxfail` — це прапорці командного рядка (див. `bash`-блоки у
головному `README.md`). Тут ми **симулюємо** їхню логіку чистими функціями, щоб
її можна було протестувати без запуску вкладеного pytest.

## Файли

- `example_1_x_concept.py` — концепція `-x` як `--maxfail=1`: скільки тестів реально виконалось до зупинки
- `example_2_maxfail_logic.py` — узагальнена логіка `--maxfail=N`
- `example_3_combine.py` — поєднання порядку (`--ff`) із зупинкою (`-x`)

## Запуск

```bash
pytest example_1_x_concept.py -v
pytest example_2_maxfail_logic.py -v
pytest example_3_combine.py -v
```

Усі тести тут **проходять** — вони демонструють, як має поводитись зупинка.
