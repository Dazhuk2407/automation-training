# Lesson 17: Markers (маркери)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Позначати тести маркерами `@pytest.mark.smoke`, `@pytest.mark.regression`
- ✅ Створювати **власні** маркери (`api`, `ui`, `critical`)
- ✅ **Реєструвати** маркери через `conftest.py` (`pytest_configure`) або `pytest.ini`
- ✅ Ставити **кілька** маркерів на один тест
- ✅ Маркувати цілий клас / файл через `pytestmark`
- ✅ Розуміти навіщо маркери — категоризація тестів для вибіркового запуску в CI

---

## 📋 Передумови

Ви вже знаєте:
- Параметризацію тестів (`@pytest.mark.parametrize`, Lesson 15)
- Data-driven підхід (Lesson 16)

Маркери — це той самий синтаксис `@pytest.mark.<name>`, що й у `parametrize`, але зі своєю метою: не «розмножити» тест, а **позначити** його «тегом».

---

## 📖 Теорія

### 1. Що таке маркер

**Маркер** — це «тег» (мітка), який ви навішуєте на тест. Він **не змінює** результат тесту: тест з маркером проходить так само, як і без нього. Маркер лише **категоризує** тест, щоб потім можна було запускати підмножини:

```bash
pytest -m smoke        # тільки smoke-тести
pytest -m "not slow"   # усе, крім повільних
```

Маркер сам по собі нічого не «робить» — це метадані. Ви (або CI) вирішуєте, що з ними робити.

---

### 2. `@pytest.mark.smoke` над тестом

Маркер — це декоратор над функцією тесту:

```python
import pytest


@pytest.mark.smoke
def test_login_page_opens():
    assert True
```

`smoke` — це готовий (уже зареєстрований у корені проєкту) маркер. Декоратор просто «чіпляє» мітку до тесту.

---

### 3. РЕЄСТРАЦІЯ маркерів (важливо!)

У цьому проєкті в кореневому `pytest.ini` увімкнено `--strict-markers`. Це означає: **будь-який маркер, який не зареєстровано, спричинить помилку** (а не просто warning). Тому власні маркери **обов'язково** реєструють.

**Спосіб A — через `conftest.py` та `pytest_configure`:**

```python
# conftest.py
def pytest_configure(config):
    config.addinivalue_line("markers", "api: тести API-рівня")
    config.addinivalue_line("markers", "ui: тести UI-рівня")
    config.addinivalue_line("markers", "critical: критичні перевірки")
```

**Спосіб B — через `pytest.ini`:**

```ini
[pytest]
markers =
    api: тести API-рівня
    ui: тести UI-рівня
    critical: критичні перевірки
```

Обидва способи рівноцінні. Формат опису однаковий: `ім'я: опис`.

> У цьому проєкті `smoke`, `regression`, `slow`, `unit`, `integration` **вже зареєстровані** глобально у кореневому `pytest.ini` — їх реєструвати не треба. А ось власні (`api`, `ui`, `critical`) реєструють у локальному `conftest.py`.

Перевірити список зареєстрованих маркерів:

```bash
pytest --markers
```

---

### 4. Кілька маркерів на одному тесті

Декоратори «стакаються» — можна навісити скільки завгодно:

```python
@pytest.mark.smoke
@pytest.mark.api
def test_health_endpoint():
    assert True
```

Тепер тест потрапить і в `pytest -m smoke`, і в `pytest -m api`. Порядок декораторів значення не має.

---

### 5. Маркер на цілому класі / файлі (`pytestmark`)

Щоб не повторювати маркер над кожним тестом, є два способи.

**На класі — декоратор над класом:**

```python
@pytest.mark.regression
class TestCheckout:
    def test_add_to_cart(self):
        assert True

    def test_apply_coupon(self):
        assert True
```

**На цілому файлі (модулі) — змінна `pytestmark`:**

```python
import pytest

pytestmark = pytest.mark.api          # один маркер на всі тести файлу
# або кілька:
pytestmark = [pytest.mark.api, pytest.mark.regression]
```

Усі тести у файлі автоматично отримають ці маркери.

---

### 6. Маркери у QA: типові категорії

У реальних проєктах маркери — це основа організації CI-пайплайнів:

| Маркер | Що позначає | Коли запускають |
|--------|-------------|-----------------|
| `smoke` | Критичний мінімум «чи взагалі працює» | На кожен коміт / PR |
| `regression` | Повний набір перевірок | Ніч / реліз |
| `slow` | Повільні тести | Окремо, щоб не гальмувати |
| `api` | Тести API-рівня | За потреби |
| `ui` | Тести UI-рівня | За потреби |
| `critical` | Найважливіші бізнес-сценарії | Обов'язково перед релізом |

Приклад CI-логіки:

```bash
pytest -m smoke                    # швидкий фідбек на PR
pytest -m "regression and not slow"  # нічний прогін без повільних
```

---

## ⚠️ Типові помилки

### Незареєстрований маркер під `--strict-markers`

```python
# ❌ Маркер 'security' не зареєстровано → pytest впаде з помилкою
@pytest.mark.security
def test_auth():
    assert True
```

```
'security' not found in `markers` configuration option
```

✅ **Виправлення:** зареєструйте маркер у `conftest.py` або `pytest.ini`.

### Одрук у назві маркера

```python
# ❌ 'smoek' — це НОВИЙ (незареєстрований) маркер, а не 'smoke'!
@pytest.mark.smoek
def test_login():
    assert True
```

Через одрук тест не потрапить у `pytest -m smoke`, а під `--strict-markers` ще й зламає збір. Маркери — це рядки, pytest не «здогадається» про ваш намір.

✅ **Виправлення:** пишіть назву точно — `@pytest.mark.smoke`.

### Занадто багато маркерів на одному тесті

```python
# ❌ Маркери суперечать одне одному й нічого не дають
@pytest.mark.smoke
@pytest.mark.slow
@pytest.mark.regression
@pytest.mark.critical
@pytest.mark.api
@pytest.mark.ui
def test_everything():
    assert True
```

✅ **Виправлення:** 1–3 змістовні маркери на тест. Маркери мають допомагати обирати тести, а не заплутувати.

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-18-run-by-marker`
