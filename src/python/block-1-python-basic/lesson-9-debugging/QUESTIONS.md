# Питання для самоперевірки - Lesson 9: Debugging

## 🧠 Debugging Mindset

1. **Підхід до пошуку помилок**
   - Ви отримали `TypeError`. Які перші 3 речі ви зробите?
   - Як систематично звужувати місце помилки у великій функції?
   - Чому варто читати traceback знизу вверх?

2. **Print vs Breakpoints**
   - Коли print() краще за breakpoints?
   - Коли breakpoints краще за print()?
   - Чому print debugging не масштабується?

3. **Типові категорії помилок**
   - Різниця між SyntaxError, TypeError, ValueError, KeyError?
   - Що таке off-by-one error? Наведіть приклад.
   - Чому логічні помилки найскладніші для пошуку?

## 🔧 Інструменти IDE

4. **Breakpoints**
   - Як поставити/видалити breakpoint?
   - Чи можна поставити conditional breakpoint? Коли це корисно?

5. **Step Execution**
   - Різниця між Step Over (F10) та Step Into (F11)?
   - Коли використовувати Step Out (Shift+F11)?

6. **Variable Inspection**
   - Як переглянути значення змінної під час паузи?
   - Що таке Watch Expression і навіщо це потрібно?

7. **Call Stack**
   - Що показує call stack?
   - Як зрозуміти з call stack, звідки була викликана поточна функція?

## ✅ Практичні завдання

8. **Прочитайте traceback:**
   ```
   Traceback (most recent call last):
     File "app.py", line 15, in process_data
       result = data['key']
   KeyError: 'key'
   ```
   - В якому файлі помилка? На якому рядку?
   - Який тип помилки? Що вона означає?
   - Як би ви це виправили?

9. **Знайдіть баг поглядом** (без запуску):
   ```python
   def average(numbers):
       total = 0
       for n in numbers:
           total += n
       return total / len(numbers)
   ```
   - Для якого вхідного значення ця функція впаде?

---

**✅ Готові до Lesson 10?** Якщо відповідаєте на більшість запитань — так!