# Lesson 06: Registration

## Goal
Automate the OpenCart **Register** flow (`index.php?route=account/register`, title `Зареєструватися`) as a real, multi-field form. You will fill **every** required field — including two `<select>` dropdowns (Country and Region/Zone) — agree to the Privacy Policy, submit `Продовжити`, and verify that OpenCart creates the account and **auto-logs the user in**. This lesson also introduces the `utils/` package: a single source of synthetic, unique-per-run registration data your later lessons will reuse. All assertions are plain pytest `assert` statements and live only in the tests.

## Theory
- A registration test is a **multi-field form flow**: fill several inputs, choose options in dropdowns, tick a checkbox, click a button, then verify the resulting state.
- On this demo store ALL of these are required: `#input-firstname`, `#input-lastname`, `#input-email`, `#input-telephone`, `#input-address-1`, `#input-city`, `#input-zone` (a `<select>`), `#input-country` (a `<select>`), `#input-password`, `#input-confirm`, plus the Privacy Policy checkbox `input[name='agree']`. Submit with the button labelled `Продовжити`. A name/email/password-only fill **fails** — Address 1, City and Zone are required too.
- A `<select>` is not a text field. You do not `fill()` it — you **choose** an option with `select_option()` (by label, value, or index). Country label `Ukraine`, zone label e.g. `Kyiv`.
- On success OpenCart shows a confirmation page and **auto-authenticates** the new user — you are logged in immediately, so account-only navigation (My Account, Logout at `index.php?route=account/logout`) becomes available.
- On problems the store renders **inline validation messages** in `.text-danger` next to the offending fields; each field has its own message. Registering the **same e-mail twice** raises a duplicate-e-mail warning — so every run needs a fresh, unique e-mail.
- Keep **test data separate from test logic**. Values you type come from `utils/data.py`, not magic strings in the test body. The password for a generated test user is ordinary **TEST DATA** — keep it in the helper/config, never in environment variables (those are for real, shared secrets) and never use real personal data.

## New Concepts
- Driving a **real multi-field form** through one Page Object method `register(user)`.
- Choosing an option in a **`<select>`** with `select_option()` (Country, Zone).
- Creating the **`utils/` package** with `unique_email()` and `generate_user_data()` (synthetic, unique-per-run data reused by later lessons).
- Reading **field-scoped `.text-danger` validation messages** and mapping field → expected message.
- A **state-integrity** scenario: register, log out, attempt a duplicate, then prove the original account still logs in.

## Practical Explanation
The `utils/` package is born here. Add an empty `utils/__init__.py` so it is importable, then a single source of registration data:

```python
# utils/data.py
import time


def unique_email(prefix: str = "user") -> str:
    # A timestamp keeps each run's e-mail unique so registration never clashes.
    return f"{prefix}_{int(time.time() * 1000)}@example.com"


def generate_user_data() -> dict:
    # One reusable source of complete, valid, SYNTHETIC registration data.
    # country/zone are REAL option labels on demo.opencart.ua (confirm in DevTools).
    return {
        "first_name": "Test",
        "last_name": "User",
        "email": unique_email(),
        "telephone": "0501234567",
        "address": "1 Test Street",
        "city": "Kyiv",
        "country": "Ukraine",     # #input-country <select> label
        "zone": "Kyiv",           # #input-zone <select> label
        "password": "Test1234!",  # synthetic test data — NOT a real secret
    }
```

The `RegisterPage` holds only locators, navigation, and actions — **no assertions**. It follows the canonical style: `super().__init__(page)` first, a `PATH` constant, a no-arg `open()`, all locators in `__init__`. Note the two `<select>` locators.

```python
# pages/register_page.py
from pages.base_page import BasePage


class RegisterPage(BasePage):
    PATH = "index.php?route=account/register"

    def __init__(self, page):
        super().__init__(page)
        self.firstname_input = page.locator("#input-firstname")
        self.lastname_input = page.locator("#input-lastname")
        self.email_input = page.locator("#input-email")
        self.telephone_input = page.locator("#input-telephone")
        self.address_input = page.locator("#input-address-1")
        self.city_input = page.locator("#input-city")
        self.country_select = page.locator("#input-country")   # <select>
        self.zone_select = page.locator("#input-zone")         # <select>
        self.password_input = page.locator("#input-password")
        self.confirm_input = page.locator("#input-confirm")
        self.agree_checkbox = page.locator("input[name='agree']")
        self.continue_button = page.get_by_role("button", name="Продовжити")
        self.errors = page.locator(".text-danger")             # all inline messages

    def open(self):
        super().open(self.PATH)

    def register(self, user):
        # One user-data dict instead of many positional parameters.
        self.firstname_input.fill(user["first_name"])
        self.lastname_input.fill(user["last_name"])
        self.email_input.fill(user["email"])
        self.telephone_input.fill(user["telephone"])
        self.address_input.fill(user["address"])
        self.city_input.fill(user["city"])
        self.country_select.select_option(label=user["country"])  # chosen, not filled
        self.zone_select.select_option(label=user["zone"])
        self.password_input.fill(user["password"])
        self.confirm_input.fill(user["password"])
        self.agree_checkbox.check()
        self.continue_button.click()
```

Assertions stay in the test, as plain `assert`. The Page Object performs the action; the data comes from `utils/`. The success heading below is an **EXAMPLE** — confirm the real text in DevTools:

```python
# tests/test_registration.py
from pages.register_page import RegisterPage
from utils.data import generate_user_data


def test_registration_creates_account(page):
    user = generate_user_data()
    register_page = RegisterPage(page)
    register_page.open()
    register_page.register(user)

    # Confirm the EXACT success heading in DevTools before finalising.
    heading = page.locator("h1")
    assert heading.is_visible()
    assert "створено" in heading.inner_text()          # "...account created"
    # Auto-login: an account-only control (Logout) is now reachable.
    assert "account/logout" in page.content()
```

Notice the shape: no `expect()` anywhere, the Page Object holds no checks, and every `assert` answers a business question ("was the account created?", "am I logged in?").

## Homework
Do all three tasks on a branch named `lesson-06`. Reuse `generate_user_data()` and `RegisterPage.register(user)` — do not re-implement form filling in each test.

### Task 1 — Complete successful registration with auto-login
#### Scenario
A new customer fills the whole registration form correctly and expects a working, already-authenticated account.
#### Preconditions
- `RegisterPage(BasePage)` exists with `register(user)` and locators for every required field, both `<select>` elements, the agree checkbox, and the submit button.
- `utils/data.py` provides `generate_user_data()` returning a complete synthetic user with a unique e-mail.
#### Steps
- Generate a fresh user with `generate_user_data()`.
- Open the register page and call `register(user)` (fills all text fields, **chooses** Country and Zone via `select_option`, ticks agree, submits `Продовжити`).
- Read the confirmation heading and the account-area state after submit.
#### Expected Results (automate as plain asserts)
- The success confirmation heading is visible and contains the created-account text (EXAMPLE `створено` — confirm exact wording in DevTools).
- The store auto-logged the user in: an account-only control is present (e.g. a Logout link / `account/logout` route is reachable, or the account dropdown is visible).
- The Country and Zone selects each carried the intended value: `register_page.country_select.input_value()` and `zone_select.input_value()` are non-empty (a `<select>` returns the chosen option's value).
#### Implementation Notes
- Extend `RegisterPage`; Country and Zone must use `select_option`, never `fill`.
- Create `utils/__init__.py` and `utils/data.py` (the `utils/` package starts this lesson).
- Confirm in DevTools: every field id, the two `<select>` option lists, `input[name='agree']`, the `Продовжити` button, and the real success heading.
#### Done When
- One test registers a uniquely generated user and passes on a fresh e-mail every run.
- Auto-login and both select values are asserted with plain `assert`, no `expect()`.

### Task 2 — Required-field validation matrix (field → message)
#### Scenario
The form must reject incomplete submissions and tell the user **exactly which** field is wrong — without raising spurious errors on fields that were filled correctly.
#### Preconditions
- `RegisterPage` from Task 1.
- A way to read the `.text-danger` message scoped to a single field (confirm the per-field message element in DevTools — it sits in each field's form-group).
#### Steps
- Build a valid user with `generate_user_data()`, then blank exactly one required **text** field (e.g. set `first_name=""`), and submit.
- Parametrize over several fields, one per row: firstname, lastname, e-mail, telephone, address, city, password.
- For each row, provide the field key **and** its expected validation message.
#### Expected Results (automate as plain asserts)
- The offending field shows its **specific** `.text-danger` message: `assert expected_message in field_error.inner_text()` (EXAMPLE messages such as `Ім'я повинно містити від 1 до 32 символів!` — confirm each in DevTools).
- At least one validation message is visible overall: `assert register_page.errors.count() > 0`.
- **No incorrect error on unrelated fields:** pick one field you filled correctly and assert its per-field error is absent/empty (e.g. `assert other_field_error.count() == 0` or `assert not other_field_error.inner_text().strip()`).
- Registration did **not** proceed: the URL still contains `account/register` (no success heading).
#### Implementation Notes
- Use `@pytest.mark.parametrize("field, message", [...])` — one row per required field, mapping field → expected message.
- Reuse `register(user)` by passing a user dict with a single blanked field; keep the two selects valid so only the target text field fails.
- Do not put the message strings in the Page Object — they are expected-value **test data** in the parametrize table.
#### Done When
- A parametrized test covers several required fields, each asserting its own message and no false error elsewhere.
- Each case appears by name in `pytest -v` (e.g. `[first_name]`, `[email]`).

### Task 3 — Duplicate e-mail & data integrity
#### Scenario
An e-mail may back exactly one account. A second registration with the same e-mail must be refused, and it must neither damage nor duplicate the original account — the original must still log in.
#### Preconditions
- `RegisterPage` from Task 1 and a `LoginPage` (or the login route `index.php?route=account/login`, `#input-email`/`#input-password`, button `Вхід`).
- Logout route `index.php?route=account/logout`.
#### Steps
- Generate one user and register successfully (Task 1 flow); remember its e-mail and password.
- Log out (open the logout route / click Logout).
- Open the register page again and attempt to register the **same** e-mail (reuse the same user dict).
- Then go to the login page and log in with the **original** e-mail + password.
#### Expected Results (automate as plain asserts)
- The duplicate attempt is refused: a duplicate-e-mail warning is visible (EXAMPLE `Ваша адреса Email вже зареєстрована!` — confirm the real text/element, e.g. an alert or `.text-danger`), and the URL still contains `account/register` (no new success page).
- The original account still works: after logging in with the original credentials, an account-only control is present and the URL reflects the authenticated account area (e.g. contains `account/account`), and the wrong-credentials warning `E-Mail і/чи пароль не співпадають.` is **absent**.
- The duplicate attempt created no usable second account: logging in with the original credentials succeeds exactly once (the state is consistent, not doubled).
#### Implementation Notes
- Reuse `generate_user_data()` and `RegisterPage.register(user)`; do not hardcode the e-mail — capture the generated one and reuse it for both the duplicate attempt and the final login.
- A short `logout()` action (navigate to the logout route) and a `login(email, password)` action belong on the relevant Page Object; assertions stay in the test.
- Confirm in DevTools: the duplicate-warning element/text, the logout link, and the authenticated account-area indicator.
#### Done When
- One end-to-end test registers, logs out, is refused on the duplicate, and logs the original account back in — all verified with plain `assert`.
- The test passes on a fresh unique e-mail every run and uses no `expect()`.

> Tip: field ids, both `<select>` option lists, the `Продовжити` button, and the exact success / duplicate-warning / validation messages can differ by store version. Open `index.php?route=account/register` in DevTools and confirm the real selectors and messages before finalising. Values marked EXAMPLE above are placeholders to verify live.

## Expected Project Structure After This Lesson
```text
opencart-qa-automation/
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
├── README.md
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── category_page.py
│   ├── product_page.py
│   ├── search_results_page.py
│   ├── register_page.py         # new this lesson
│   └── login_page.py            # new this lesson (used by Task 3)
├── utils/                       # new this lesson: the utils/ package starts here
│   ├── __init__.py
│   └── data.py                  # unique_email() + generate_user_data()
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    ├── test_locators.py
    ├── test_assertions.py
    ├── test_search.py
    └── test_registration.py     # new this lesson
```

## Git Workflow Reminder
Work on branch `lesson-06`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Automate a real multi-field form end to end through a single Page Object `register(user)` method, keeping the form logic out of the tests.
- Choose options in `<select>` dropdowns (Country, Zone) with `select_option` instead of `fill`, and read the chosen value with `input_value()`.
- Create the `utils/` package and generate unique, synthetic test data (a fresh e-mail per run) reused across lessons.
- Build a parametrized field → message validation matrix that also proves unrelated fields show no false errors.
- Verify a state-integrity scenario — register, log out, reject a duplicate, and confirm the original account still logs in — using only plain pytest `assert` (no `expect()`), with all assertions in the tests.
