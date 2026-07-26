# Питання для самоперевірки — Lesson 57: Logging

1. **Чому `logging` кращий за `print`?** (рівні, формат, керованість, вимкнення без видалення коду)
2. **Назвіть п'ять рівнів logging за зростанням важливості.** (`DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`)
3. **Яке число відповідає рівню `WARNING`?** (30)
4. **Що робить `logging.basicConfig(level=..., format=...)`?**
5. **Що означає плейсхолдер `%(levelname)s` у форматі?**
6. **Навіщо `logger = logging.getLogger(__name__)` замість `logging.info(...)`?**
7. **Чому `logger.info("User %s created", name)` краще за конкатенацію рядків?** (lazy форматування)
8. **Який рівень використати для падіння тесту, а який для нестабільності?**
9. **Чому не можна використовувати `logging.warn`?** (deprecated, треба `warning`)
10. **Як перевірити повідомлення логу в pytest?** (fixture `caplog`)

---

**Далі:** `lesson-58-project-structure`
