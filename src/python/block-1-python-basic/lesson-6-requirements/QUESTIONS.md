# Питання для самоперевірки - Lesson 6: requirements.txt

## 🎯 requirements.txt

1. **Чому потрібен requirements.txt?**
   - Як це допомагає командній роботі?
   - Навіщо його робити?

2. **pip freeze**
   - Команда для генерування файлу
   - Що розміщується у файлі?

3. **Встановлення залежностей**
   - Команда для встановлення з файлу
   - Як встановити на новій машині?

4. **Оновлення**
   - Як оновити залежності у файлі?
   - Як оновити встановлені пакети?

## ✅ Практичні завдання

5. **Генеруйте файл:**
   ```bash
   pip freeze > requirements.txt
   ```

6. **Перегляньте вміст:**
   ```bash
   cat requirements.txt
   ```

7. **Встановіть з файлу:**
   ```bash
   pip install -r requirements.txt
   ```

8. **Оновіть залежності:**
   ```bash
   pip install --upgrade -r requirements.txt
   pip freeze > requirements.txt  # Оновіть файл
   ```

---

**✅ Коли requirements.txt працює - переходьте до Lesson 7**
