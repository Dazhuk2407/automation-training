# Завдання 02 — Check Box

## Мета
Розгорнути дерево, обрати чекбокс та перевірити блок результату.

## URL
https://demoqa.com/checkbox

## Кроки
1. Відкрити сторінку.
2. Розгорнути все дерево — клік по `button[title="Expand all"]`.
3. Клікнути по чекбоксу ноди **Desktop**:
   `page.locator('label[for="tree-node-desktop"] .rct-checkbox').click()`

## Що перевірити (через `assert`)
- Блок `#result` видимий.
- Текст `#result` містить `desktop`.
- Інпут `#tree-node-desktop` у стані `checked`.

## Підказки
- Дочекатися появи результату: `page.locator("#result").wait_for(state="visible")`
- DemoQA рендерить імена у результаті малими літерами без пробілів.
- `assert page.locator("#result").is_visible()`
- `assert "desktop" in page.locator("#result").text_content()`
- `assert page.locator("#tree-node-desktop").is_checked()`

## Запуск
```bash
pytest src/ui_practice_tasks/task_02_check_box -v
```

## Готово, коли
- Тест зелений.
- 3 перевірки через `assert`.
- При зміні очікуваного тексту тест падає.