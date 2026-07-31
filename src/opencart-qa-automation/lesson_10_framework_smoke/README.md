# Lesson 10: Regression & Framework Quality

## Goal
This is the **capstone** lesson, continuing from Lessons 00–09 and reusing the complete framework you already built — `BasePage`, every page object, `config.py` (`BASE_URL = "https://demo.opencart.ua"`), `utils/data.py` (`unique_email()`, `generate_user_data()`), and the `conftest.py` fixtures (`logged_in_page` and `cart_with_product`, both from Lesson 08). You will not add a new feature. Instead you will make the framework *professional*: classify every test as **smoke** or **regression** by business risk and document why; assemble one **critical end-to-end regression** that walks a real customer journey through the page objects and fixtures you already own; then run a **stability and maintainability audit** that removes duplication, brittle selectors, and hidden cross-test dependencies, guarantees unique user data and isolated fixture state, and finishes with a **portfolio README**. By the end this repository is a project you can confidently show an employer.

## Theory
- A **marker** is a label attached with `@pytest.mark.<name>` so you can **select a subset** without moving files. Register markers in `pytest.ini` and add `--strict-markers` so a typo (`@pytest.mark.smok`) becomes an **error**, not a silent new marker.
- **`smoke`** = a small, fast "is the site fundamentally alive?" set (home loads, search works, add-to-cart, login). **`regression`** = the broader, slower set covering details, edge cases, and end-to-end journeys. Select with `pytest -m smoke` or `pytest -m "not smoke"`.
- **Risk-based classification** means the label reflects *business risk*, not convenience: if a broken check would stop customers from buying, it is smoke. Documenting the choice in the README turns the marker scheme into something a teammate can trust.
- **Test independence** means each test sets up its own state and passes when run **alone**. Hidden dependencies (a reused account, a cart another test populated, an ordering assumption) cause flaky failures — and they are exactly what breaks parallel execution.
- **Refactor** = improving structure **without changing behaviour**. Repeated lines belong in `BasePage` or a fixture. Run the full suite green **before** and **after** every refactoring step. Assertions stay in tests as plain `assert`; page objects hold only locators, navigation, and actions.

## New Concepts
- **Risk-based marker classification**: choosing `smoke` vs `regression` by business impact and documenting the rationale.
- **Registering markers** in `pytest.ini` (`[pytest] markers = ...`) with `--strict-markers`.
- **A critical end-to-end regression**: chaining register → login → search → product → cart → quantity update → total validation → logout through existing page objects/fixtures.
- **Stability audit**: proving each test passes alone and as a suite; removing duplication, brittle selectors, and hidden dependencies.
- **Isolated fixture state** and **unique user data** as the foundation of safe parallelism.
- Writing a **portfolio-quality repository README**.

## Practical Explanation
Assertions here are ordinary Python `assert` statements in the test files — no `expect()`. Page objects expose read-back helpers; the test decides what is correct.

### 1. Tag a test with a risk-based marker
One decorator line per label; a test can carry both.

```python
# tests/test_search.py  (illustrative — you tag your own tests)
import pytest
from pages.home_page import HomePage


@pytest.mark.smoke          # fast, high business risk -> smoke
@pytest.mark.regression
def test_search_returns_matching_products(page):
    home_page = HomePage(page)
    home_page.open()
    home_page.search("iphone")
    assert "product/search" in page.url
    assert home_page.result_cards.count() > 0
```

### 2. Register the markers in `pytest.ini`
`--strict-markers` turns an unknown or mistyped marker into an error instead of a warning.

```ini
# pytest.ini
[pytest]
addopts = --strict-markers
markers =
    smoke: fast, high-value checks of the core journeys (run these first)
    regression: broader, slower checks of details, edge cases, and end-to-end flows
```

### 3. Run a subset by marker
```bash
pytest -m smoke            # only the smoke suite (fast feedback)
pytest -m regression      # only regression
pytest -m "not smoke"     # everything except smoke
pytest                    # the whole suite
```

### 4. Chain existing page objects into one end-to-end flow
The end-to-end regression writes **no** new register/login/cart mechanics — it *reuses* what you already built. Fixtures supply the starting state; the test drives the journey and asserts with plain `assert`.

```python
# tests/test_regression.py  (illustrative — not the homework solution)
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.mark.regression
def test_end_to_end_purchase_journey(logged_in_page):
    page = logged_in_page                 # fixture already registered a fresh unique user
    # ... search -> open product -> add to cart -> update qty -> validate total -> logout ...
    cart = CartPage(page)
    unit_price = cart.line_unit_price(0)  # read the displayed unit price first
    cart.set_quantity(0, 2)
    cart.update()
    expected_total = round(unit_price * 2, 2)
    assert cart.line_total(0) == expected_total   # derived, not hardcoded
```

### 5. Refactor duplicated steps upward — behaviour-preserving
If many tests repeat the same navigation, promote it once into `BasePage`. Locators still live inside each page object; only shared *behaviour* moves up.

```python
# pages/base_page.py  (shared helper — assertions still live in tests)
from config import BASE_URL


class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, path=""):
        """Navigate to BASE_URL + path — reused instead of repeating this everywhere."""
        url = f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}"
        self.page.goto(url)
```

> Tip: run the full suite **before** you touch anything and **again after** — the same tests must still pass. Refactor in small commits so any regression is easy to spot. Routes, titles, and selectors can differ by store version/language, so confirm them in DevTools.

### Professional Tip: Parallel Test Execution *(optional — not homework)*
A ~30-test UI suite runs one test at a time by default. Once your tests are truly **independent**, run them **in parallel** with **`pytest-xdist`**. Add it to `requirements.txt`, reinstall, then:

```bash
pytest -n auto            # spread tests across all available CPU cores
```

`-n auto` picks a worker count from your CPUs (or pass a number, e.g. `-n 4`). Parallel workers run in a **non-deterministic order and at the same time**, so any **shared state** — a reused account, a cart left populated by another test, an ordering assumption — causes flaky **parallel-only failures**. This is exactly why Task 1 insists smoke tests pass **alone** and Task 3 audits for isolation. Independence is what makes parallelism safe. Treat this as a habit to explore, not a required deliverable.

## Homework
Do all three tasks on a branch named `lesson-10`. This is the final lesson — aim for a repository you would proudly show an employer.

### Task 1 — Risk-based smoke / regression classification
#### Scenario
A team needs fast feedback: before running the whole suite they want a small, trustworthy set that answers "can a customer still use the store at all?". You classify every existing test by **business risk** and make the scheme selectable and documented.
#### Preconditions
- Lessons 00–09 tests exist and pass.
- You can run `pytest` locally against `BASE_URL`.
#### Steps
1. Register `smoke` and `regression` in `pytest.ini` and add `--strict-markers` to `addopts`.
2. Review **every** existing test. Decide its risk: would a failure block a customer from browsing, finding, or buying? High-risk core journeys (home loads, search works, add-to-cart, login) get `@pytest.mark.smoke`; the broader detail/edge-case tests get `@pytest.mark.regression`. A test may carry both.
3. Run `pytest -m smoke` and count the selected tests; run `pytest -m "not smoke"` for the rest.
4. Run each smoke test **on its own** (e.g. by node id) to confirm it does not silently depend on another test.
#### Expected Results (automate/verify)
- `pytest -m smoke` selects **only** the smoke-tagged tests (verify the count matches your tagging).
- `pytest --strict-markers` reports **no** unknown-marker warnings.
- Each smoke test **passes when run alone** — no cross-test dependency.
#### Implementation Notes
Markers and `pytest.ini` are the mechanism. The deliverable is the *classification plus its rationale*: add a short **"Test classification"** section to the README explaining why each marker choice reflects business risk. No new page object is needed. Confirm smoke-critical selectors still match the live store (header search `input[name='search']`, cart badge `#cart`).
#### Done When
- `smoke` and `regression` are registered with `--strict-markers`; no marker warnings.
- Every test is tagged by business risk; `pytest -m smoke` runs only that subset.
- Each smoke test passes independently.
- The README explains the marker rationale.

### Task 2 — Critical end-to-end regression journey
#### Scenario
The single most valuable regression is the full purchase path a real customer takes. You automate it end to end so one failing check flags a broken buying flow immediately — **reusing** the page objects and fixtures you already built, never re-implementing setup.
#### Preconditions
- All page objects from Lessons 01–09 exist (`HomePage`, `SearchResultsPage`, `ProductPage`, `CartPage`, `RegisterPage`, `LoginPage`, `AccountPage`).
- `conftest.py` provides `logged_in_page` and `cart_with_product`; `utils/data.py` provides `generate_user_data()` / `unique_email()`.
#### Steps
1. **Register** a fresh unique user (reuse `generate_user_data()` + `RegisterPage.register(user)`, or start from the `logged_in_page` fixture which already does this) — the account auto-authenticates.
2. **Log out**, then **log in** again with the same credentials to prove the account persists.
3. **Search** for a known product name and open it from the results (**open product**).
4. **Add to cart**, then open the cart.
5. **Update the quantity** on the cart line to 2 and apply the update.
6. **Validate the total**: read the displayed unit price *before* changing quantity, derive the expected line total in the test, and compare against the displayed total after the update.
7. **Log out** and confirm the session ended.
#### Expected Results (automate as plain asserts)
- After re-login, an authenticated marker is present (e.g. `assert account.logout_link.is_visible()` or account route reachable).
- The opened product matches the searched name (`assert product_name in product.title_text()`).
- The cart contains the added product after add-to-cart.
- The line total recalculates: `assert cart.line_total(0) == round(unit_price * 2, 2)` — **derived**, not hardcoded.
- After logout, protected state is gone (e.g. account route redirects to Login / login control reappears).
#### Implementation Notes
Chain the **existing** page objects and the `logged_in_page` fixture — do **not** copy register/login/cart code into this test. If `CartPage` lacks quantity-input, update-button, or line-total/unit-price read-back helpers, add those **locators/methods** to `CartPage` (locators stay in the page object; the arithmetic and assertions stay in the test). Tag the test `@pytest.mark.regression`. Read the price *before* clicking so the expected value is derived from live data, not a constant.
#### Done When
- One end-to-end test performs register → logout → login → search → open product → add to cart → update quantity → validate total → logout.
- It reuses page objects and fixtures with **no duplicated setup code**.
- The total assertion is derived from the displayed unit price, not hardcoded.
- The test is tagged `regression` and passes on its own.

### Task 3 — Stability & maintainability audit + portfolio README
#### Scenario
Before calling the framework "done", you make it *trustworthy*: it must pass identically whether tests run one at a time or all together, contain no copy-pasted setup or fragile selectors, and leave no test depending on another's leftovers. Then you present it as a portfolio piece.
#### Preconditions
- Tasks 1 and 2 are complete; the suite is green.
- You can run individual tests and the full suite.
#### Steps
1. Run the **whole** suite (`pytest`), then run tests **individually** (and try a shuffled/parallel run, e.g. `pytest -n auto`). Compare results — any test that only passes in a certain order has a hidden dependency.
2. **Remove duplication**: move repeated navigation/waits/common setup into `BasePage` or `conftest.py` fixtures, keeping the suite green after each step.
3. **Remove brittle selectors**: replace index-based or auto-generated-attribute locators with stable ones (roles, names, IDs, scoped `.product-thumb` queries); confirm each in DevTools.
4. **Eliminate hidden dependencies**: ensure every test creates the state it needs. Generated user data must be **unique** per test (`unique_email()` / `generate_user_data()`), and fixtures must yield **isolated** state (a fresh user / a clean cart) so no test inherits another's data.
5. Write the **portfolio README** at the repo root: stack (Python, Playwright, pytest), project structure, how to run all tests, and how to run smoke vs regression.
#### Expected Results (verify)
- The full suite and individual runs produce the **same** pass results (order-independent).
- No duplicated setup blocks remain; shared behaviour lives in `BasePage`/fixtures.
- No index-fragile or auto-generated-attribute selectors remain in the audited tests.
- Every registration/login test uses **unique** user data; fixtures create isolated state.
- The root `README.md` documents stack, structure, run-all, and smoke-vs-regression.
#### Implementation Notes
This is a refactor: **behaviour must not change** — the same tests pass before and after. Work in small commits so any regression is easy to bisect. The `pytest -n auto` parallel run is a *diagnostic* for hidden shared state, not a required deliverable. Finish by pushing `lesson-10` and opening the final Pull Request into `main`.
#### Done When
- The suite passes both individually and as a group, order-independent.
- Duplication and brittle selectors are removed; the suite stays green.
- User data is unique and fixtures are isolated (no hidden cross-test state).
- The root `README.md` is portfolio-quality (stack, structure, how to run, smoke vs regression).
- `lesson-10` is pushed and the final PR into `main` is opened.

## Expected Project Structure After This Lesson
```text
opencart-qa-automation/
├── config.py
├── conftest.py                  # fixtures: logged_in_page, cart_with_product, shared setup
├── pytest.ini                   # markers registered here (smoke, regression) + --strict-markers
├── requirements.txt             # + pytest-xdist (optional parallel-execution tip)
├── .gitignore
├── README.md                    # portfolio README: stack, structure, how to run, smoke vs regression
├── pages/
│   ├── base_page.py             # refactor target: shared navigation/helpers live here
│   ├── home_page.py
│   ├── category_page.py
│   ├── product_page.py
│   ├── search_results_page.py
│   ├── register_page.py
│   ├── login_page.py
│   ├── account_page.py
│   ├── cart_page.py             # + quantity input, update button, unit-price/line-total read-back
│   └── wishlist_page.py
├── utils/
│   └── data.py                  # unique_email(), generate_user_data()
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    ├── test_locators.py
    ├── test_assertions.py
    ├── test_search.py
    ├── test_registration.py
    ├── test_login.py
    ├── test_cart.py
    ├── test_wishlist.py
    ├── test_account.py
    └── test_regression.py       # new this lesson: critical end-to-end journey
```

## Git Workflow Reminder
Work on branch `lesson-10`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Classify tests as `smoke` or `regression` by **business risk** and register those markers in `pytest.ini` with `--strict-markers`.
- Run a targeted subset with `pytest -m smoke` or `pytest -m "not smoke"` for fast feedback, and document the rationale.
- Automate a **critical end-to-end regression** (register → login → search → product → cart → quantity → total → logout) by reusing existing page objects and fixtures — no duplicated setup.
- Derive expected values (like a recalculated line total) from live data instead of hardcoding them.
- Audit a suite for **stability and maintainability**: order-independence, no duplication, no brittle selectors, unique user data, isolated fixtures.
- Understand how `pytest-xdist` (`pytest -n auto`) parallelises an independent suite and why shared state breaks it.
- Present the whole project with a portfolio-quality README.

---

Congratulations! You have built a **portfolio-ready OpenCart automation framework** — page objects, isolated fixtures, a risk-based marker scheme, a critical end-to-end regression, and a suite that passes independently and together. This repository is now a project you can confidently show an employer. Well done.
