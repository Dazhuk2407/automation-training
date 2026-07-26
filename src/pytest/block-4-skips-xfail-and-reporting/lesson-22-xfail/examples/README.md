# Приклади — Lesson 22: xfail

У цій папці — робочі приклади до Lesson 22. Усі файли дають **0 failures**
(статуси `xfailed` / `xpassed` — це НЕ failure).

## Файли

- `example_1_xfail_basic.py` — xfail-тест, що реально падає → статус `xfailed`
- `example_2_xfail_reason.py` — xfail з `reason` поряд зі звичайними passing-тестами
- `example_3_xpass_strict.py` — `xpass` (xfail-тест, що проходить) + пояснення `strict`

## Як запускати

```bash
pytest example_1_xfail_basic.py -v
pytest example_2_xfail_reason.py -v
pytest example_3_xpass_strict.py -rX -v   # -rX показує причини xpassed
```

Прапорці для звіту:
- `-rx` — показати причини `xfailed`
- `-rX` — показати причини `xpassed`
- `-ra` — показати все (skip / xfail / xpass тощо)
