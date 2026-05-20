# Завдання 05 — Web Tables

## Мета
Додати нового користувача через модалку та перевірити, що рядок зʼявився у таблиці.

## URL
https://demoqa.com/webtables

## Кроки
1. Відкрити сторінку.
2. Клікнути кнопку **Add** → `#addNewRecordButton`.
3. Заповнити поля модалки:
   - `#firstName` → `Alice`
   - `#lastName` → `Cooper`
   - `#userEmail` → `alice.cooper@example.com`
   - `#age` → `28`
   - `#salary` → `45000`
   - `#department` → `QA`
4. Натиснути Submit у модалці → `#submit`.

## Що перевірити (через `assert`)
- Модалка `#registration-form-modal` прихована (hidden).
- Таблиця `.rt-tbody` містить `alice.cooper@example.com`.
- Таблиця `.rt-tbody` містить `Alice`.

## Підказки
- Дочекатися закриття модалки:
  `page.locator("#registration-form-modal").wait_for(state="hidden")`
- `assert page.locator("#registration-form-modal").is_hidden()`
- `assert "alice.cooper@example.com" in page.locator(".rt-tbody").text_content()`
- Поля `#age` та `#salary` приймають рядок з цифрами: `.fill("28")`.

## Запуск
```bash
pytest src/ui_practice_tasks/task_05_web_tables -v
```

## Готово, коли
- Тест зелений.
- 3 перевірки через `assert`.
- При зміні очікуваного email тест падає.