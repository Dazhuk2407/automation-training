# Завдання 01 — Text Box

## Мета
Заповнити форму та перевірити, що введені дані відображаються у блоці результату.

## URL
https://demoqa.com/text-box

## Кроки
1. Відкрити сторінку.
2. Заповнити поля:
   - Full Name → `#userName`
   - Email → `#userEmail`
   - Current Address → `#currentAddress`
   - Permanent Address → `#permanentAddress`
3. Натиснути кнопку Submit → `#submit`.

## Тестові дані
- Full Name: `John Carton`
- Email: `john.carton@example.com`
- Current Address: `123 Main St`
- Permanent Address: `456 Other St`

## Що перевірити (через `assert`)
- Блок `#output` видимий.
- `#output #name` містить `John Carton`.
- `#output #email` містить `john.carton@example.com`.
- `#output #currentAddress` містить `123 Main St`.
- `#output #permanentAddress` містить `456 Other St`.

## Підказки
- `page.locator("#userName").fill("John Carton")`
- Перед перевіркою результат може ще не відрендеритись — дочекайся:
  `page.locator("#output").wait_for(state="visible")`
- `assert page.locator("#output").is_visible()`
- `assert "John Carton" in page.locator("#output #name").text_content()`
- Якщо кнопку Submit перекриває банер: `page.locator("#submit").scroll_into_view_if_needed()`.

## Запуск
```bash
pytest src/ui_practice_tasks/task_01_text_box -v
```

## Готово, коли
- Тест зелений.
- 5 перевірок через `assert`.
- При зміні очікуваного тексту на неправильний — тест падає.