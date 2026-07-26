# Приклади — Lesson 14: Fixture Best Practices

## Файли

- `example_1_isolation.py` — ізоляція: function-scope дає свіжі дані кожному тесту (4 тести)
- `example_2_minimal_scope.py` — мінімальний scope: function за замовчуванням, session лише для дорогого read-only ресурсу (4 тести)
- `example_3_single_responsibility.py` — одна відповідальність, композиція `user → client → authed_session`, зрозумілі імена (4 тести)

## Як працювати

1. Запустіть кожен приклад і подивіться, що всі тести проходять:
   ```bash
   pytest example_1_isolation.py -v
   pytest example_2_minimal_scope.py -v
   pytest example_3_single_responsibility.py -v
   ```
2. У `example_1_isolation.py` зверніть увагу: два тести мутують ту саму фікстуру, але не впливають один на одного.
3. У `example_3_single_responsibility.py` простежте, як фікстури компонуються шар за шаром замість одного «комбайна».
