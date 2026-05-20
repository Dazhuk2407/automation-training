# Завдання 06 — Practice Form

## Мета
Заповнити форму та перевірити дані у модальному вікні після сабміту.

## URL
https://demoqa.com/automation-practice-form

## Тестові дані
- First Name: `John`
- Last Name: `Carton`
- Email: `john.carton@example.com`
- Gender: `Male`
- Mobile: `1234567890`
- Current Address: `123 Main St`

## Кроки
1. Відкрити сторінку.
2. Заповнити `#firstName`, `#lastName`, `#userEmail`.
3. Обрати стать: `page.get_by_text("Male", exact=True).click()`
4. Заповнити `#userNumber` (рівно 10 цифр).
5. Заповнити `#currentAddress`.
6. Прокрутити до кнопки та клікнути Submit:
   - `page.locator("#submit").scroll_into_view_if_needed()`
   - `page.locator("#submit").click(force=True)`
   - `force=True` потрібен, бо внизу сторінки є банер реклами, що може перекривати кнопку.

## Що перевірити (через `assert`)
- Модалка `.modal-content` видима.
- Заголовок `#example-modal-sizes-title-lg` дорівнює `Thanks for submitting the form`.
- `.modal-body` містить `John Carton`.
- `.modal-body` містить `john.carton@example.com`.
- `.modal-body` містить `1234567890`.

## Підказки
- Дочекатися появи модалки:
  `page.locator(".modal-content").wait_for(state="visible")`
- `assert page.locator(".modal-content").is_visible()`
- `assert page.locator("#example-modal-sizes-title-lg").text_content() == "Thanks for submitting the form"`
- `assert "John Carton" in page.locator(".modal-body").text_content()`
- Радіо-кнопки приховані за label — клікай по тексту.

## Запуск
```bash
pytest src/ui_practice_tasks/task_06_practice_form -v
```

## Готово, коли
- Тест зелений.
- 5 перевірок через `assert`.
- При зміні очікуваних даних тест падає.