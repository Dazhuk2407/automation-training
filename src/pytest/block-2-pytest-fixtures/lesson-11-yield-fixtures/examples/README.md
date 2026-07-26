# Приклади — Lesson 11: yield Fixtures

У цій папці — робочі приклади yield-фікстур. Усі тести проходять.

## Файли

- `example_1_yield_basic.py` — базова yield-фікстура: setup → yield → teardown
- `example_2_teardown_order.py` — порядок teardown при кількох фікстурах (LIFO)
- `example_3_resource.py` — імітація ресурсу (з'єднання, тимчасовий файл через `tmp_path`)

## Запуск

```bash
pytest example_1_yield_basic.py -v
pytest example_2_teardown_order.py -v
pytest example_3_resource.py -v
```
