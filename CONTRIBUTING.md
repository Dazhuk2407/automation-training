# CONTRIBUTING.md

## Як вносити свій внесок у проект

### Процес розробки

1. **Форкніть репозиторій** (якщо не маєте доступу)
2. **Створіть нову гілку** для вашої функції:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Внесіть зміни** та коміти:
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Запустіть тести**:
   ```bash
   pytest
   ```
5. **Спушите вашу гілку**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Створіть Pull Request**

### Конвенції для комітів

Використовуйте наступний формат для повідомлень про комміти:

```
<type>: <subject>

<body>

<footer>
```

**Type:** Add, Fix, Update, Remove, Refactor, Docs, Style, Test, Chore

**Приклади:**
- `Add: lesson on decorators in Python basics`
- `Fix: test failures in pytest fixtures`
- `Update: Playwright examples for version 1.40`
- `Docs: add missing sections to Git guide`

### Стиль коду

- Дотримуйтесь PEP 8
- Використовуйте 4 пробіли для відступів
- Максимальна довжина рядка: 100 символів
- Документуйте функції та класи

### Тестування

- Напишіть тести для нових функцій
- Переконайтеся, що всі тести проходять:
  ```bash
  pytest
  ```
- Отримайте покриття тестами (мінімум 80%):
  ```bash
  pytest --cov
  ```

### Структура гілок

- `main` - стабільна версія
- `develop` - розробка
- `feature/*` - нові функції
- `fix/*` - виправлення помилок
- `docs/*` - документація

