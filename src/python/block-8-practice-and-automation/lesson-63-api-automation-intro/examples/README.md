# Приклади — Lesson 63: API Automation Intro

- `example_1_http_basics.py` — основи HTTP як чисті функції (status_class, is_success, ...)
- `example_2_mock_client.py` — MockApiClient (get/post) з заданими відповідями
- `example_3_api_test.py` — приклад API-тесту (arrange-act-assert) + авторизація через env

> Приклади НЕ роблять реальних HTTP-запитів і НЕ використовують мережу — лише mock-клієнт.

```bash
pytest example_1_http_basics.py -v
pytest example_2_mock_client.py -v
pytest example_3_api_test.py -v
```
