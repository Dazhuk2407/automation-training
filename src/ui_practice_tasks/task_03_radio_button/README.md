# Завдання 03 — Radio Button

## Мета
Обрати доступну радіокнопку та перевірити результат.

## URL
https://demoqa.com/radio-button

## Кроки
1. Відкрити сторінку.
2. Клікнути по тексту **Yes** (інпут прихований за label):
   `page.get_by_text("Yes", exact=True).click()`

## Що перевірити (через `assert`)
- `#yesRadio` у стані `checked`.
- Текст у `.text-success` містить `Yes`.
- `#noRadio` у стані `disabled`.

## Підказки
- Дочекатися появи тексту результату:
  `page.locator(".text-success").wait_for(state="visible")`
- `assert page.locator("#yesRadio").is_checked()`
- `assert "Yes" in page.locator(".text-success").text_content()`
- `assert page.locator("#noRadio").is_disabled()`

## Запуск
```bash
pytest src/ui_practice_tasks/task_03_radio_button -v
```

## Готово, коли
- Тест зелений.
- 3 перевірки через `assert`.
- При зміні очікуваного тексту тест падає.