# Lesson 07: Login

## Goal
This lesson continues from Lessons 00–06, reusing your `BasePage`, page objects, `config.py`, `conftest.py`, and the Lesson 06 `utils/data.py` helpers (`unique_email()`, `generate_user_data()`, and `RegisterPage.register(user)`). Here your framework learns to **authenticate**: drive the OpenCart login form, tell an authenticated header from an anonymous one, prove that a protected page is gated behind login, and log out again. By the end you will have a `LoginPage`, an `AccountPage` (which owns `logout()` plus the header account/Logout locators), and a `tests/test_login.py` covering a positive session, an invalid-credential matrix, and a full session-state transition.

## Theory
- **Login page**: route `index.php?route=account/login`, title `Авторизація` — an E-Mail field `#input-email`, a Password field `#input-password`, and a submit button labelled `Вхід`. A successful login lands on the account dashboard `index.php?route=account/account`.
- **A positive login needs an account that already exists** — but registration on this demo **auto-authenticates** the new user, so right after registering you are already logged in and there is nothing to "log in" to. The reliable, self-contained flow is therefore: **register a fresh unique user → log OUT → open the Login page → log in with the same credentials.** That guarantees a real, isolated positive-login test that does not depend on any pre-existing account.
- **Failed login** (unknown e-mail, wrong password, or blank fields) keeps you on the login page and shows a warning in `.alert-danger` with the exact text `E-Mail і/чи пароль не співпадають.` A refused login never reaches `account/account`.
- **Authenticated vs anonymous header**: when logged in, an account menu with a **Вихід** (Logout) link is present; when logged out, the **Login/Register** options return. This visible difference is how a test proves a session started or ended.
- **A protected page proves the session server-side.** The Wishlist route `index.php?route=account/wishlist` requires login: while authenticated it opens normally, but once you log out the same route **redirects to the Login page**. This is a stronger signal than header state alone.
- **`logout()` lives on `AccountPage`**, not on `LoginPage` — the page that represents the signed-in area owns the action that ends the session.
- Test-generated passwords are ordinary **test data** — they come from `generate_user_data()`, never from real personal credentials and never from environment variables (those are for real/shared secrets).

> **No login fixture yet.** A reusable `logged_in_page` fixture is introduced in **Lesson 08**. In this lesson every test drives register → logout → login (or register → authenticated) by hand, so you can see each step.

## New Concepts
- Automating a login form: fill E-Mail + Password, click `Вхід`, land on the account dashboard.
- Handling **auto-authentication after registration** — logging out first so a positive login test is meaningful.
- Distinguishing **authenticated vs anonymous** header state through visible controls.
- **Parametrizing a negative matrix** with `@pytest.mark.parametrize` (unknown e-mail, wrong password, empty e-mail, empty password, both empty) so five cases share one test body.
- Verifying an **authorization gate**: a protected route is reachable while logged in and **redirects to Login** once logged out.
- A dedicated **`AccountPage`** that owns `logout()` and the header account/Logout locators.

## Practical Explanation
Both page objects follow the canonical style: inherit `BasePage`, call `super().__init__(page)` first, define **all** locators in `__init__`, expose a `PATH` constant and a no-arg `open()`, and keep **assertions out of the page** — they live in the test as plain `assert` statements. Selectors you have not personally verified — the account menu and the Logout label — are shown as **examples**; confirm them in DevTools.

```python
# pages/login_page.py
from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "index.php?route=account/login"

    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.locator("#input-email")
        self.password_input = page.locator("#input-password")
        self.login_button = page.get_by_role("button", name="Вхід")
        self.warning = page.locator(".alert-danger")

    def open(self):
        super().open(self.PATH)

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
```

`AccountPage` represents the signed-in area and owns the header account menu, the Logout action, and (for reading anonymous state) the header Login/Register locators:

```python
# pages/account_page.py
from pages.base_page import BasePage


class AccountPage(BasePage):
    PATH = "index.php?route=account/account"

    def __init__(self, page):
        super().__init__(page)
        # Header top-right account dropdown — EXAMPLE selector, confirm in DevTools.
        self.account_menu = page.locator("a[title='Мій обліковий запис']")
        # Logout link inside that menu — EXAMPLE label, confirm in DevTools.
        self.logout_link = page.get_by_role("link", name="Вихід")
        # Anonymous-header controls that reappear after logout — EXAMPLE, confirm.
        self.register_link = page.get_by_role("link", name="Реєстрація")

    def open(self):
        super().open(self.PATH)

    def logout(self):
        self.account_menu.click()
        self.logout_link.click()
```

Assertions are ordinary `assert` statements in the test — **no `expect()` anywhere**. For example, a positive login checks the route and a visible account-only control:

```python
# tests/test_login.py (positive — sketch, not the full homework)
from pages.register_page import RegisterPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from utils.data import generate_user_data


def test_login_succeeds_with_valid_credentials(page):
    user = generate_user_data()

    # 1) Register (this auto-authenticates the user).
    RegisterPage(page).open()
    RegisterPage(page).register(user)

    # 2) Log OUT so we can test a real login.
    account_page = AccountPage(page)
    account_page.logout()

    # 3) Log IN with the same credentials.
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["email"], user["password"])

    assert "account/account" in page.url
    assert account_page.logout_link.is_visible()
```

Note the shape: `AccountPage` performs the logout action, `LoginPage` performs the login action, the data comes from `generate_user_data()`, and the plain `assert` checks stay in the test. Each assertion answers a business question ("did we reach the account area?", "is the session-ending control present?").

## Homework

Extend `tests/test_login.py` with the three scenarios below. All assertions are plain `assert` statements in the test file; page objects hold only locators and actions.

### Task 1 — Positive login session
#### Scenario
A returning customer with a real account signs in and reaches their account area with the authenticated navigation available. This is the core happy-path login journey.
#### Preconditions
A registered account whose credentials you control. Because registration auto-authenticates, create it in-test and log out first so the login step is genuine.
#### Steps
1. Generate a fresh user with `generate_user_data()` and register via `RegisterPage.register(user)` (auto-authenticates).
2. Log out through `AccountPage.logout()` so the session is truly ended.
3. Open the Login page and call `LoginPage.login(user["email"], user["password"])`.
#### Expected Results
- After login the URL contains `account/account` (the account dashboard was reached).
- An authenticated-only control is present, e.g. `account_page.logout_link.is_visible()` is `True`.
- The account-area heading/content is non-empty (`assert <heading>.inner_text().strip()`), confirming a real signed-in page rendered, not a redirect back to Login.
#### Implementation Notes
- Create `pages/login_page.py` (`LoginPage(BasePage)` with `PATH`, no-arg `open()`, and `login(email, password)`).
- Reuse the Lesson 06 `RegisterPage` + `generate_user_data()`; use the `AccountPage.logout()` you build in Task 3 (or stub the logout locators first and share them).
- No fixture — the test drives register → logout → login itself.
#### Done When
- `LoginPage.login()` fills `#input-email` + `#input-password` and clicks `Вхід`.
- The test registers, logs out, logs back in, and asserts `account/account` in the URL plus a visible authenticated control.
- DevTools-confirmed selectors; the test passes on a fresh run.

### Task 2 — Invalid-credential matrix
#### Scenario
The login form must refuse bad input and always give the same generic warning, without leaking whether the e-mail or the password was the problem. You verify five failure variants in one parametrized test.
#### Preconditions
On the Login page. One row (wrong password) needs an e-mail that actually exists — register a fresh user first and reuse that e-mail; the other rows use deliberately bad or empty values.
#### Steps
1. Register a fresh user with `generate_user_data()` so you have one real e-mail on record; log out.
2. Parametrize a test over these five cases (email, password): **unknown e-mail** + any password; **known e-mail** + wrong password; **empty e-mail** + some password; some e-mail + **empty password**; **both empty**.
3. For each row: open the Login page and submit the pair via `LoginPage.login(...)`.
#### Expected Results
- For every row the URL is **not** `account/account` (login refused — still on the login page).
- The `.alert-danger` warning is visible and its text contains `E-Mail і/чи пароль не співпадають.`
- No account-only control (e.g. the Logout link) becomes visible for any row.
#### Implementation Notes
- Use `@pytest.mark.parametrize` with the five (email, password) rows so one test body covers all cases.
- Assert with plain `assert`, e.g. `assert login_page.warning.is_visible()` and `assert "E-Mail і/чи пароль не співпадають." in login_page.warning.inner_text()`.
- Do not add assertions just to raise the count — the route check, the message check, and the no-session check are the three business questions.
#### Done When
- One parametrized test runs all five rows and each asserts refusal + the exact warning + no authenticated state.
- DevTools-confirmed `.alert-danger` message; the test passes.

### Task 3 — Session state transition
#### Scenario
A session is real only if it gates protected content. You prove the full lifecycle: logged in → a protected page opens → logout → the same protected page redirects to Login and the account-only controls disappear.
#### Preconditions
An authenticated page. Register a fresh user with `generate_user_data()` (auto-authenticates) — no separate login step needed to reach the logged-in state.
#### Steps
1. Register a fresh user (now authenticated).
2. Open the protected **Wishlist** route (`index.php?route=account/wishlist`) and confirm it renders as the wishlist, not the Login page.
3. Capture that an account-only control (e.g. the Logout link) is visible.
4. Call `AccountPage.logout()`.
5. Attempt to open the same Wishlist route again while now anonymous.
#### Expected Results
- **While logged in:** the Wishlist URL contains `account/wishlist` and does **not** redirect to `account/login`; the Logout link is visible.
- **After logout:** opening the Wishlist route lands on the Login page — `assert "account/login" in page.url`.
- The account-only control is gone (`assert account_page.logout_link.is_visible() is False`) and an anonymous control returns (e.g. `assert account_page.register_link.is_visible()`).
#### Implementation Notes
- Create `pages/account_page.py` (`AccountPage(BasePage)`) owning the account-menu, Logout, and an anonymous-header (Login/Register) locator, plus `logout()`.
- Reuse (or lightly extend) your Lesson 09 wishlist route knowledge here only as a **protected page** — no `WishlistPage` object is required; opening the raw route via `BasePage.open(path)` is enough.
- Keep all state checks as plain `assert` in the test; the page objects only navigate and act.
#### Done When
- `AccountPage.logout()` opens the account menu and clicks `Вихід`.
- The test asserts the protected page is reachable while logged in and redirects to Login after logout, and that account-only controls disappear while anonymous controls return.
- DevTools-confirmed account-menu, Logout, and Login/Register selectors; the tests pass.

> Tip: the account-menu selector, the `Вихід` label, and the Login/Register labels are shown as **examples** — open the logged-in and logged-out headers in DevTools and confirm the real selectors and the warning text before finalizing.

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
│   ├── register_page.py
│   ├── login_page.py         # new this lesson
│   └── account_page.py       # new this lesson: logout() + header account/Logout/Login-Register locators
├── utils/
│   └── data.py               # unique_email(), generate_user_data() — reused from Lesson 06
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    ├── test_locators.py
    ├── test_assertions.py
    ├── test_search.py
    ├── test_registration.py
    └── test_login.py         # new this lesson: positive session, invalid matrix, session transition
```

## Git Workflow Reminder
Work on branch `lesson-07`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Automate an OpenCart login flow with a `LoginPage(BasePage)` page object using plain `assert` checks (no `expect()`).
- Handle registration's auto-authentication by logging out first, so a positive login test is meaningful.
- Distinguish authenticated from anonymous header state through visible controls.
- Parametrize an invalid-credential matrix and assert the exact `E-Mail і/чи пароль не співпадають.` warning in `.alert-danger` while confirming no session started.
- Verify an authorization gate: a protected route opens while logged in and redirects to Login after logout.
- Perform logout through a dedicated `AccountPage.logout()` and verify the full logged-in → logged-out session transition.
