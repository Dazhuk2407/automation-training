# Приклади — Lesson 60: File Paths

- `example_1_abs_rel.py` — абсолютні vs відносні шляхи, cwd
- `example_2_script_relative.py` — шлях відносно скрипта через `Path(__file__)`
- `example_3_safe_paths.py` — resolve, безпечне з'єднання, path traversal

```bash
pytest example_1_abs_rel.py -v
pytest example_2_script_relative.py -v
pytest example_3_safe_paths.py -v
```
