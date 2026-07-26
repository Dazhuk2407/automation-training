# Приклади — Lesson 56: pip and requirements

- `example_1_parse_requirements.py` — парсинг рядка та тексту `requirements.txt`
- `example_2_version_specifiers.py` — класифікація специфікаторів версій
- `example_3_freeze_diff.py` — діф двох наборів `freeze` (додано/видалено/змінено)

> Приклади лише **парсять рядки** — жодних реальних `pip`-викликів чи мережі.

```bash
pytest example_1_parse_requirements.py -v
pytest example_2_version_specifiers.py -v
pytest example_3_freeze_diff.py -v
```
