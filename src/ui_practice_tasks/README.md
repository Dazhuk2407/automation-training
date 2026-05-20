# UI Practice Tasks — Playwright + Pytest

6 незалежних практичних завдань на сайті [https://demoqa.com](https://demoqa.com).
Кожен учень виконує **одне** завдання — таски не повʼязані між собою.

API: **синхронний** (`from playwright.sync_api import sync_playwright`).
Перевірки — через звичайний `assert` (як у pytest).

## Перелік

| №  | Папка                  | Тема                  |
|----|------------------------|-----------------------|
| 01 | `task_01_text_box`     | Заповнення інпутів    |
| 02 | `task_02_check_box`    | Чекбокс у дереві      |
| 03 | `task_03_radio_button` | Радіокнопки           |
| 04 | `task_04_buttons`      | Click / dblclick / RC |
| 05 | `task_05_web_tables`   | Додавання у таблицю   |
| 06 | `task_06_practice_form`| Велика форма + модалка|

## Налаштування (нагадування)

Передбачається, що `.venv` уже створено і активовано.

```bash
pip install -r requirements.txt
playwright install chromium
```

Активація venv (якщо потрібно):
- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- **Windows (cmd):** `.venv\Scripts\activate.bat`
- **macOS:** `source .venv/bin/activate`

## Запуск одного завдання

```bash
pytest src/ui_practice_tasks/task_01_text_box -v
```

Заміни `task_01_text_box` на потрібну папку.

## Як виглядає мінімальний тест

```python
from playwright.sync_api import sync_playwright


def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # видимий браузер
        page = browser.new_page()

        # 1. Arrange — відкрити сторінку
        page.goto("https://demoqa.com/text-box")

        # 2. Act — заповнити / клікнути
        page.locator("#userName").fill("John")
        page.locator("#submit").click()

        # 3. Assert — перевірити
        page.locator("#output").wait_for(state="visible")
        assert "John" in page.locator("#output #name").text_content()

        browser.close()
```

## Шпаргалка по локаторах та діях

```python
# Локатори (як знайти елемент)
page.locator("#some-id")                          # за id
page.locator(".some-class")                       # за class
page.get_by_text("Submit", exact=True)            # за видимим текстом
page.get_by_role("button", name="Click Me")       # за роллю

# Дії
page.locator("#userName").fill("значення")        # заповнити інпут
page.locator("#submit").click()                   # клік
page.locator("#btn").dblclick()                   # подвійний клік
page.locator("#btn").click(button="right")        # правий клік
page.locator("#btn").scroll_into_view_if_needed() # прокрутити до елемента
page.locator("#btn").click(force=True)            # клік навіть якщо щось перекриває
```

## Шпаргалка по перевірках через `assert`

```python
locator = page.locator("#some-id")

# Перед перевіркою — дочекайся елемента, якщо він зʼявляється не миттєво:
locator.wait_for(state="visible")   # або "hidden"

# Видимість
assert locator.is_visible()
assert locator.is_hidden()

# Текст (точний / підрядок)
assert locator.text_content() == "Очікуваний текст"
assert "John" in locator.text_content()

# Стан інпутів
assert locator.is_checked()
assert locator.is_disabled()
assert locator.is_enabled()

# Значення поля вводу
assert locator.input_value() == "John"
```