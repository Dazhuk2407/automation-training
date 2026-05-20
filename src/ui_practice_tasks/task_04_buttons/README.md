# Завдання 04 — Buttons

## Мета
Виконати три типи кліку та перевірити повідомлення під кнопками.

## URL
https://demoqa.com/buttons

## Кроки
1. Відкрити сторінку.
2. Подвійний клік по `#doubleClickBtn`:
   `page.locator("#doubleClickBtn").dblclick()`
3. Правий клік по `#rightClickBtn`:
   `page.locator("#rightClickBtn").click(button="right")`
4. Звичайний клік по кнопці **Click Me**:
   `page.get_by_role("button", name="Click Me", exact=True).click()`

## Що перевірити (через `assert`)
- `#doubleClickMessage` має текст `You have done a double click`.
- `#rightClickMessage` має текст `You have done a right click`.
- `#dynamicClickMessage` має текст `You have done a dynamic click`.

## Підказки
- Дочекатися появи повідомлення перед `assert`:
  `page.locator("#doubleClickMessage").wait_for(state="visible")`
- `assert page.locator("#doubleClickMessage").text_content() == "You have done a double click"`
- `.dblclick()` — це не два `.click()`.
- Правий клік: параметр `button="right"` у методі `.click()`.
- `exact=True` потрібен, інакше Playwright знайде декілька кнопок з підрядком "Click Me".

## Запуск
```bash
pytest src/ui_practice_tasks/task_04_buttons -v
```

## Готово, коли
- Тест зелений.
- 3 перевірки через `assert`.
- При зміні очікуваного тексту тест падає.