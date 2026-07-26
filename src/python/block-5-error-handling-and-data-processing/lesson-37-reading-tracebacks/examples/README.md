# Приклади — Lesson 37: Reading Tracebacks

- `example_1_read_traceback.py` — захоплення traceback та його складові (тип, меседж)
- `example_2_traceback_module.py` — модуль `traceback`: `format_exc` для логування
- `example_3_nested_calls.py` — ланцюг викликів A → B → C у traceback

```bash
pytest example_1_read_traceback.py -v
pytest example_2_traceback_module.py -v
pytest example_3_nested_calls.py -v
```
