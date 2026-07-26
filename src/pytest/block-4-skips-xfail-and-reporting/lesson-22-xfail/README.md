# Lesson 22: Expected Failures (@pytest.mark.xfail)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Позначати очікуване падіння через `@pytest.mark.xfail(reason=...)`
- ✅ Розуміти статуси `xfailed` (очікувано впав) та `xpassed` (несподівано пройшов)
- ✅ Використовувати умовний xfail (`@pytest.mark.xfail(condition, reason=...)`)
- ✅ Знати `strict=True` (xpass стає failure)
- ✅ Розрізняти `xfail` і `skip`

---

## 📋 Передумови

Ви вже знаєте:
- Як пропускати тести через `@pytest.mark.skip` та `@pytest.mark.skipif` (Lesson 21)
- Як писати маркери та assertions (Lesson 5, 6)

Skip **не виконує** тест. Тепер розберемо `xfail` — маркер, який **виконує** тест, але очікує, що він **впаде**.

---

## 📖 Теорія

### 1. Що таке xfail

`xfail` = **eXpected FAILure** (очікуване падіння).

Це спосіб сказати pytest: **«цей тест ЗАРАЗ падає, і це очікувано»**.

Типова ситуація в QA:
- Знайдено баг, заведено тікет `bug #123`
- Баг ще **не пофіксили**
- Тест на цей баг **падає** — і це правильно, бо баг реальний

Якщо просто залишити тест падаючим — CI буде червоним, і серед реальних падінь загубиться відомий баг. `xfail` розв'язує це: тест виконується, падає, але позначається як `xfailed`, а не `failed`.

```python
import pytest

@pytest.mark.xfail(reason="bug #123: округлення daє неправильний результат")
def test_known_bug():
    assert round(2.675, 2) == 2.68   # падає → xfailed, не failure
```

---

### 2. @pytest.mark.xfail(reason=...) — базовий синтаксис

```python
@pytest.mark.xfail(reason="bug #123")
def test_feature():
    ...
```

Що робить pytest:
1. **Виконує** тіло тесту (на відміну від skip).
2. Якщо тест **падає** → статус `xfailed` (**не** failure).
3. У підсумку: `1 xfailed`, exit code = 0.

`reason` — **обов'язковий за домовленістю**: він пояснює, ЧОМУ тест падає (номер тікета, посилання на баг). Без нього незрозуміло, що це за очікуване падіння.

Вивід pytest:

```
test_feature.py::test_feature XFAIL (bug #123)
========== 1 xfailed in 0.01s ==========
```

---

### 3. xpass — тест несподівано ПРОЙШОВ

`xpass` = **unexpectedly passing** (несподівано пройшов).

Якщо тест позначений `xfail`, але **пройшов** — це `xpassed`.

```python
@pytest.mark.xfail(reason="можливо вже пофіксили")
def test_maybe_fixed():
    assert 1 == 1   # проходить → xpassed
```

Що це означає? Ймовірно, **баг уже пофіксили**, а маркер `xfail` забули прибрати.

**За замовчуванням `xpass` — НЕ failure** (exit code = 0):

```
test_maybe_fixed.py::test_maybe_fixed XPASS (можливо вже пофіксили)
========== 1 xpassed in 0.01s ==========
```

---

### 4. strict=True — xpass стає FAILURE

Проблема xpass за замовчуванням: він «тихий». Легко забути прибрати `xfail` після фіксу бага.

`strict=True` робить `xpass` **справжнім failure**:

```python
@pytest.mark.xfail(reason="bug #123", strict=True)
def test_feature():
    assert result == expected
```

- Тест падає → `xfailed` (ок, exit code 0).
- Тест проходить → **`FAILED`** (exit code 1) з повідомленням `[XPASS(strict)]`.

Це **сигнал**: баг пофіксили → пора прибрати маркер `xfail` і залишити звичайний тест. `strict=True` — рекомендована практика для QA, бо не дає забути мертвий маркер.

> Можна ввімкнути глобально в `pytest.ini`: `xfail_strict = true`.

---

### 5. Умовний xfail

Іноді тест падає **лише за певних умов** (ОС, версія Python, залежність). Перший позиційний аргумент `xfail` — це **умова**:

```python
import sys

@pytest.mark.xfail(sys.platform == "win32", reason="не працює на Windows")
def test_platform_specific():
    ...
```

- Якщо умова `True` → маркер активний (очікуємо падіння).
- Якщо умова `False` → маркер ігнорується, тест звичайний.

Це те саме, що `skipif`, але тест усе одно **виконується** (коли умова істинна).

---

### 6. xfail vs skip

| | `skip` / `skipif` | `xfail` |
|---|---|---|
| Тіло тесту виконується? | ❌ Ні | ✅ Так |
| Коли використовувати | фіча ще не написана / не застосовна | баг відомий, тест падає |
| Тест падає | залишається skipped | `xfailed` (не failure) |
| Тест проходить | залишається skipped | `xpassed` (або failure зі strict) |

**Головна відмінність:** `skip` НЕ виконує код тесту взагалі. `xfail` ВИКОНУЄ код і очікує, що він впаде.

Правило вибору:
- Фічі **ще немає** → `skip`.
- Фіча є, але **зламана (баг)** → `xfail`.

---

### 7. xfail у роботі QA

Реальний сценарій:

1. Тестувальник знаходить баг, заводить тікет `JIRA-456`.
2. Пише тест, який відтворює баг. Тест **падає** (баг реальний).
3. Позначає його `@pytest.mark.xfail(reason="JIRA-456", strict=True)`.
4. CI стає **зеленим** — але баг **видимий** у звіті (`1 xfailed`).
5. Розробник фіксить баг → тест починає проходити → `xpass` зі `strict` робить CI **червоним**.
6. Це сигнал прибрати `xfail`: тепер це звичайний регресійний тест.

Так відомий баг не блокує пайплайн, але й не губиться.

---

## ⚠️ Типові помилки

### xfail без reason

```python
# ❌ Незрозуміло, ЧОМУ тест падає
@pytest.mark.xfail
def test_something():
    ...

# ✅ Завжди вказуйте причину (номер тікета)
@pytest.mark.xfail(reason="bug #123: some description")
def test_something():
    ...
```

### xfail замість skip для ненаписаної фічі

```python
# ❌ Фічі ще немає — xfail тут неправильний
@pytest.mark.xfail(reason="фіча ще не реалізована")
def test_new_feature():
    ...

# ✅ Ненаписана фіча = skip
@pytest.mark.skip(reason="фіча ще не реалізована")
def test_new_feature():
    ...
```

`xfail` — для **існуючого зламаного** коду, а не для того, чого ще немає.

### Забути прибрати xfail після фіксу

```python
# ❌ Баг пофіксили, тест проходить, але маркер лишився → тихий xpass
@pytest.mark.xfail(reason="bug #123")
def test_fixed_bug():
    assert now_works()

# ✅ strict=True зробить xpass видимим (FAILED) і нагадає прибрати маркер
@pytest.mark.xfail(reason="bug #123", strict=True)
def test_fixed_bug():
    assert now_works()
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-23-last-failed`
