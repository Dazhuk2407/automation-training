# Приклади — Lesson 55: Modules and Packages

- `helpers.py` — власний модуль-приклад (не тест)
- `mypackage/` — пакет із модулями `calc.py`, `strings.py`
- `example_1_use_module.py` — імпорт власного модуля
- `example_2_package_import.py` — імпорт із пакета
- `example_3_module_attributes.py` — `__name__` та атрибути модуля

```bash
pytest example_1_use_module.py -v
pytest example_2_package_import.py -v
pytest example_3_module_attributes.py -v
```
