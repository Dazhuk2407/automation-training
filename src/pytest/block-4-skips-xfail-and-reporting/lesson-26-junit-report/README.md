# Lesson 26: JUnit XML Report — базовий звіт для CI

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Генерувати JUnit XML звіт командою `pytest --junitxml=report.xml`
- ✅ Розуміти структуру JUnit XML (`testsuite`, `testcase`, `failure`, `skipped`)
- ✅ Парсити звіт і рахувати результати (tests / failures / skipped / passed)
- ✅ Розуміти навіщо JUnit XML у CI (Jenkins, GitLab, GitHub Actions)
- ✅ Знати про `--junit-prefix` та альтернативи (HTML-звіти оглядово)

---

## 📋 Передумови

Ви вже знаєте:
- Як запускати тести з CLI та читати вивід (Lesson 7-8)
- Як обробляти дані у Python (словники, цілі числа, рядки)

Тепер ми навчимось перетворювати результати тестів у **машинно-читабельний звіт**, який розуміють CI/CD системи.

---

## 📖 Теорія

### 1. Навіщо потрібні звіти

Коли ви запускаєте `pytest` локально — ви бачите результат у терміналі. Але у CI/CD (Jenkins, GitLab CI, GitHub Actions) **немає людини**, яка читає термінал. Системі потрібні результати у **стандартному машинно-читабельному форматі**.

JUnit XML — це такий стандарт. Спочатку він з'явився у світі Java (JUnit), але став де-факто універсальним: майже кожна CI-система вміє його читати і показувати pass/fail на дашборді.

**Ідея:** pytest виконує тести → записує результат у XML → CI читає XML → показує зелений/червоний білд.

---

### 2. Як згенерувати JUnit XML

Достатньо однієї опції:

```bash
pytest --junitxml=report.xml
```

Pytest виконає всі тести і додатково запише файл `report.xml` у стандартному JUnit-форматі. Термінальний вивід при цьому не змінюється — звіт створюється **на додачу**.

Шлях може бути будь-яким:

```bash
pytest --junitxml=reports/results.xml
```

Опція `--junit-prefix=NAME` додає префікс до імен усіх тестів у звіті (зручно коли кілька наборів тестів зливаються в один звіт):

```bash
pytest --junitxml=report.xml --junit-prefix=integration
```

---

### 3. Структура JUnit XML

Кореневий елемент — `<testsuite>` з атрибутами-лічильниками. Усередині — по одному `<testcase>` на кожен тест. Якщо тест впав — усередині `<testcase>` з'являється `<failure>`; якщо пропущений — `<skipped>`.

```xml
<testsuite name="pytest" tests="4" failures="1" skipped="1">
    <testcase classname="test_math" name="test_a"/>
    <testcase classname="test_math" name="test_b">
        <failure message="assert 5 == 10">AssertionError</failure>
    </testcase>
    <testcase classname="test_math" name="test_c">
        <skipped message="not ready"/>
    </testcase>
    <testcase classname="test_math" name="test_d"/>
</testsuite>
```

Ключові атрибути `<testsuite>`:

| Атрибут | Значення |
|---------|---------|
| `tests` | Загальна кількість тестів |
| `failures` | Скільки впало (`assert` не пройшов) |
| `errors` | Скільки з помилкою в коді (до assert) |
| `skipped` | Скільки пропущено |

**Важливо:** `passed` окремого атрибута НЕ має. Його рахують формулою:

```
passed = tests - failures - errors - skipped
```

---

### 4. Хто читає JUnit XML

| Система | Що робить зі звітом |
|---------|--------------------|
| Jenkins | Плагін "JUnit" показує тренди pass/fail між білдами |
| GitLab CI | Вкладка "Tests" у merge request з розбивкою по тестах |
| GitHub Actions | Дії на кшталт `test-reporter` малюють таблицю результатів |

Усі вони читають один і той самий формат. Тому `--junitxml` — універсальний спосіб "віддати" результати у пайплайн незалежно від CI-системи.

---

### 5. Парсинг звіту для власної обробки

Іноді потрібно обробити звіт самостійно — наприклад, порахувати статистику або надіслати в Slack. Для цього використовують **XML-парсер** зі стандартної бібліотеки — `xml.etree.ElementTree`:

```python
import xml.etree.ElementTree as ET

def parse_summary(xml_text):
    root = ET.fromstring(xml_text)
    return {
        "tests": int(root.get("tests")),
        "failures": int(root.get("failures")),
        "skipped": int(root.get("skipped")),
    }
```

`ET.fromstring()` парсить XML-рядок і повертає кореневий елемент. `.get("tests")` читає атрибут. Щоб пройтися по окремих тестах — `root.findall("testcase")`.

---

### 6. Альтернативи (оглядово)

Крім JUnit XML існують людино-орієнтовані звіти: `pytest-html` генерує самодостатній HTML-файл для перегляду в браузері, а Allure будує інтерактивний дашборд з кроками і скриншотами.

---

### 7. JUnit XML у QA-пайплайні

На практиці звіт — це **артефакт** CI-джоби: pytest генерує `report.xml`, CI зберігає його як artifact і парсить для відображення. Типовий крок пайплайну:

```bash
pytest --junitxml=report.xml    # згенерувати
# CI: upload report.xml as artifact + parse for the Tests tab
```

Так команда бачить історію результатів, а впалі тести підсвічуються прямо у merge request.

---

## ⚠️ Типові помилки

### Плутати шлях до report.xml

```bash
# ❌ Згенерували в один шлях, а CI шукає в іншому
pytest --junitxml=out/report.xml
# CI: artifacts: report.xml   ← не знайде, файл у out/

# ✅ Один і той самий шлях у команді та в конфізі CI
pytest --junitxml=report.xml
```

### Комітити report.xml у репозиторій

```bash
# ❌ report.xml — це згенерований артефакт, не вихідний код
git add report.xml

# ✅ Додайте у .gitignore
echo "report.xml" >> .gitignore
```

### Парсити XML регекспом замість парсера

```python
# ❌ Крихко: зламається на переносах, атрибутах, вкладеності
import re
tests = re.search(r'tests="(\d+)"', xml_text)

# ✅ Використовуйте справжній XML-парсер
import xml.etree.ElementTree as ET
tests = int(ET.fromstring(xml_text).get("tests"))
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**🎉 Вітаємо — ви завершили курс Pytest for QA!**
