# Lesson 1: Основи Playwright

## Що таке Playwright?

Playwright - це фреймворк для автоматизації браузерів (Chrome, Firefox, Safari).
Розроблений Microsoft, простіший за Selenium.

## Встановлення

```bash
pip install playwright
playwright install  # Встановить браузери
```

## Основні концепції

### Синхронний код
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    title = page.title()
    browser.close()
```

## Запуск браузера

```python
# Launch browser
browser = playwright.chromium.launch(headless=False)

# Create page
page = browser.new_page()

# Navigate
page.goto("https://example.com")

# Close
browser.close()
```

## Пошук елементів

```python
# CSS selector
element = page.query_selector("h1")
elements = page.query_selector_all("button")

# Locator API (новіший спосіб)
element = page.locator("h1")
```

## Взаємодія з елементами

```python
# Click
page.click("button")

# Type text
page.fill("input[type='text']", "Hello")

# Get text
text = page.text_content("h1")
```

## Приклади

Див. папку `examples/`

## Вправи

Виконайте завдання в папці `exercises/`

