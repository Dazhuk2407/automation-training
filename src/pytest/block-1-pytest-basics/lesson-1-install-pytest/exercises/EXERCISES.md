# Вправи — Lesson 1: Встановлення Pytest

---

## 🏋️ Вправа 1: Встановити pytest (EASY)

**Завдання:** Встановіть pytest у своє віртуальне середовище та перевірте.

```bash
# 1. Переконайтесь що venv активований
which python

# 2. Встановіть pytest
python -m pip install pytest

# 3. Перевірте версію
pytest --version
```

**Очікуваний результат:**
```
pytest 8.x.x
```

---

## 🏋️ Вправа 2: Зафіксувати залежності (EASY)

**Завдання:** Створіть `requirements.txt` з поточними залежностями.

```bash
# 1. Зафіксуйте залежності
python -m pip freeze > requirements.txt

# 2. Перевірте вміст файлу
cat requirements.txt
```

**Очікуваний результат:** файл `requirements.txt` містить pytest та його залежності з зафіксованими версіями.

---

## 🏋️ Вправа 3: Встановити додатковий плагін (MEDIUM)

**Завдання:** Встановіть `pytest-cov` (плагін для coverage) та оновіть `requirements.txt`.

```bash
# 1. Встановіть pytest-cov
python -m pip install pytest-cov

# 2. Перевірте що він з'явився
python -m pip show pytest-cov

# 3. Оновіть requirements.txt
python -m pip freeze > requirements.txt

# 4. Перевірте що pytest-cov є у файлі
cat requirements.txt
```

---

## 🏋️ Вправа 4: Відтворити середовище з нуля (MEDIUM)

**Завдання:** Перевірте що ваш `requirements.txt` дійсно працює — відтворіть середовище.

```bash
# 1. Деактивуйте поточне середовище
deactivate

# 2. Видаліть venv
rm -rf venv

# 3. Створіть заново
python3 -m venv venv
source venv/bin/activate

# 4. Встановіть з requirements.txt
python -m pip install -r requirements.txt

# 5. Перевірте що все на місці
pytest --version
python -m pip list
```

**Очікуваний результат:** pytest та pytest-cov встановлені з тими самими версіями, що й раніше.

**Чому це важливо:** Це стандартний workflow в будь-якому проєкті. Якщо `requirements.txt` не відтворює середовище — це баг.

---

## ✅ Перевірка

### Критерії:

- [ ] pytest встановлений та `pytest --version` працює
- [ ] `requirements.txt` створений і містить зафіксовані версії
- [ ] pytest-cov встановлений
- [ ] Середовище відтворюється з `requirements.txt`