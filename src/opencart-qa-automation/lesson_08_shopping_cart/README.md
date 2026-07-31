# Lesson 08: Shopping Cart

## Goal
This lesson continues from Lessons 00–07, reusing your `BasePage`, page objects, `config.py`, `conftest.py`, and the `utils/data.py` helpers. Here you automate the heart of the shopping journey: **add a product and prove the cart holds exactly what you chose**, **change quantity and verify the total the store shows equals the total you calculate**, and **drive the cart through several state transitions** (add → remove one line → remove the last line → empty cart). You will extend `ProductPage`, build a `CartPage`, and — from now on for the rest of the course — introduce two **state-building fixtures** in `conftest.py`: `logged_in_page` and `cart_with_product`.

## Theory
- The cart is **stateful**: `add → view → change quantity → remove` — each step changes state the next step reads, so order matters and tests can pollute each other unless each starts from a known state (that is what fixtures give you).
- Product page (`/desktops/test`, **Apple Cinema 30"**): quantity `input[name='quantity']`, Add-to-Cart `#button-cart`. A successful add shows a green `.alert-success` and updates the header cart badge `#cart`.
- Cart page: route `index.php?route=checkout/cart`, title `Кошик`. Each product is a **line-item row** with its own quantity field, an **update** control and a **remove** control. Prices render as text like `$122.00`; to compute with them you must strip the currency symbol and parse a number.
- **Totals are derived, never hard-coded.** Read the unit price and quantity from the page, compute `expected = unit_price * quantity` in the test, then compare against the store's displayed total. This catches real pricing bugs and survives demo-data changes.
- The empty cart shows the exact message `Ваш кошик порожній!` and the header badge resets (to `0`/empty).
- **State-building fixtures** (in `conftest.py`, no `fixtures/` directory): `logged_in_page` yields an already-authenticated page (registration auto-logs the user in); `cart_with_product` yields a page that already holds one product.

## New Concepts
- Extending `ProductPage` with an `add_to_cart(quantity=1)` action and reading its result (`.alert-success`, `#cart` badge).
- A `CartPage(BasePage)` exposing line-item rows, per-row name/price/quantity, an update action, a remove action, and the empty-cart message.
- **Parsing money**: turning `"$122.00"` into a float so the test can do arithmetic and compare totals.
- Writing **state-building fixtures** in `conftest.py` with `generate_user_data()` + `RegisterPage.register(user)`, and reusing them across tests.
- Verifying **before/after state transitions**: line count and badge value changing as items are added and removed.

## Practical Explanation
Canonical Page Object style everywhere: inherit `BasePage`, call `super().__init__(page)` first, put **all locators in `__init__`**, expose only actions (assertions live in tests), and open with a no-arg `open()`. Selectors you have not personally verified are shown as **examples** — confirm them in DevTools.

### Extend `ProductPage` with `add_to_cart()`
```python
# pages/product_page.py  (extend your existing class)
from pages.base_page import BasePage


class ProductPage(BasePage):
    PATH = "desktops/test"   # Apple Cinema 30" demo product

    def __init__(self, page):
        super().__init__(page)
        # ... existing locators (H1, price, tabs) ...
        self.quantity_input = page.locator("input[name='quantity']")
        self.add_to_cart_button = page.locator("#button-cart")
        self.success_alert = page.locator(".alert-success")
        self.cart_badge = page.locator("#cart")

    def open(self):
        super().open(self.PATH)

    def add_to_cart(self, quantity=1):
        self.quantity_input.fill(str(quantity))
        self.add_to_cart_button.click()   # -> green success alert appears
```

### A small `CartPage(BasePage)` and a money parser
```python
# pages/cart_page.py
from pages.base_page import BasePage


class CartPage(BasePage):
    PATH = "index.php?route=checkout/cart"

    def __init__(self, page):
        super().__init__(page)
        self.rows = page.locator("table tbody tr")             # line items
        # EXAMPLE per-row controls — confirm real selectors in DevTools:
        self.quantity_inputs = page.locator("input[name^='quantity']")
        self.update_buttons = page.locator("button[data-original-title='Оновити']")
        self.remove_buttons = page.locator("button[data-original-title='Видалити']")
        self.empty_message = page.get_by_text("Ваш кошик порожній!")

    def open(self):
        super().open(self.PATH)

    def update_first_quantity(self, quantity):
        self.quantity_inputs.first.fill(str(quantity))
        self.update_buttons.first.click()

    def remove_first_item(self):
        self.remove_buttons.first.click()


def parse_price(text):
    """'$122.00' -> 122.0 . Keep helpers like this out of the assertions."""
    return float(text.replace("$", "").replace(",", "").strip())
```
> The per-row update/remove tooltips and the quantity name pattern above are **examples** — OpenCart encodes each cart line's id into these controls and the labels vary by store version. Inspect a real row on `checkout/cart` and confirm the selectors yourself; that is exactly the QA skill this lesson trains.

### Two state-building fixtures in `conftest.py`
All shared fixtures live in `conftest.py`. `logged_in_page` is **self-contained**: it builds unique data with `generate_user_data()` and registers via the full form, which auto-authenticates the user.
```python
# conftest.py
import pytest
from pages.register_page import RegisterPage
from pages.product_page import ProductPage
from utils.data import generate_user_data


@pytest.fixture
def logged_in_page(page):
    user = generate_user_data()          # synthetic first/last name, unique email, telephone, address...
    register_page = RegisterPage(page)
    register_page.open()
    register_page.register(user)         # full valid form -> OpenCart auto-authenticates
    yield page                           # tests receive an already-authenticated page


@pytest.fixture
def cart_with_product(page):
    product_page = ProductPage(page)
    product_page.open()
    product_page.add_to_cart()           # arrange: exactly one item in the cart
    yield page                           # test starts from a known cart state
```
> `register(user)` must fill every required field on this demo — first/last name, e-mail, telephone, **address line 1, city, the zone `<select>` and country `<select>`**, password, confirm — and tick the Privacy-Policy checkbox before submitting `Продовжити`. Reuse the `RegisterPage` from Lesson 06.

### Assertions stay in the test (plain `assert`, no `expect`)
```python
# tests/test_cart.py (sketch — not the full homework)
from pages.product_page import ProductPage


def test_add_shows_success_and_badge(page):
    product_page = ProductPage(page)
    product_page.open()
    product_page.add_to_cart()

    assert product_page.success_alert.is_visible()
    assert "1" in product_page.cart_badge.inner_text()
```

## Homework
Do all three tasks on a branch named `lesson-08`. Use plain `assert` only — do **not** use `expect(...)`. Keep every locator inside a Page Object and every assertion inside the test.

### Task 1 — Product-to-cart consistency
#### Scenario
A shopper picks a product, adds it, and opens the cart. The cart must contain **the same product** they chose, in the **quantity** they chose — no substitution, no phantom lines.
#### Preconditions
On the Apple Cinema 30" product page (`/desktops/test`); the cart empty at the start of the test.
#### Steps
1. Open the product page and **read and save** the product name (H1) and the unit price **before** adding.
2. Add the product to the cart (quantity 1).
3. Confirm the add succeeded (success alert + header badge).
4. Open the cart page.
#### Expected Results (automate as plain asserts)
- The success alert `.alert-success` is visible after the add.
- The header cart badge `#cart` reflects one item.
- The cart has exactly **one** line-item row.
- The cart line's product name equals the name you saved before adding.
- The cart line's quantity equals `1`.
#### Implementation Notes
Extend `ProductPage` with `add_to_cart(quantity=1)` and the `.alert-success` / `#cart` locators. Create `CartPage(BasePage)` (canonical style: `PATH` + no-arg `open()`, all locators in `__init__`) exposing `rows` and per-row name/quantity. Save the name into a variable in the test and compare after navigating — do **not** hard-code `"Apple Cinema 30"` as the expected value (read it from the page). Confirm the row and quantity selectors in DevTools.
#### Done When
- `add_to_cart()` and the two new `ProductPage` locators exist; `CartPage` exists in canonical style.
- The test compares the saved product name against the cart line name and asserts quantity `1` and a single row.
- The test passes on a fresh run.

### Task 2 — Quantity and calculated totals
#### Scenario
A shopper changes the quantity of a cart line and updates the cart. The **total the store displays** for that line must equal `unit_price × quantity` — the arithmetic the customer expects.
#### Preconditions
Reuse the `cart_with_product` fixture so the test starts with one product already in the cart.
#### Steps
1. Open the cart and **read the unit price** of the line (parse `"$122.00"` → number).
2. Change the line quantity to a value greater than 1 (e.g. `3`) and click **update**.
3. Re-read the line **total** the store now displays (parse it to a number).
4. **Compute** the expected total in the test: `expected = unit_price * new_quantity`.
#### Expected Results (automate as plain asserts)
- After update, the line quantity field shows the new quantity (`input_value()`).
- The displayed line total equals your **computed** `expected` total (compare numbers; allow a tiny float tolerance).
- The unit price is unchanged by the quantity update.
#### Implementation Notes
Add an `update_first_quantity(quantity)` action and per-row price/total locators to `CartPage`. Put a `parse_price()` helper in `pages/cart_page.py` or `utils/` — it is a helper, **not** an assertion, so it lives outside the test; the test only does the final `assert`. Derive `expected` from the value you actually read; do **not** hard-code a dollar amount. Confirm the quantity input, update button, and total cell selectors in DevTools.
#### Done When
- `CartPage.update_first_quantity()` and the price/total locators exist; a `parse_price()` helper exists.
- The test computes the expected total from the read unit price and asserts it equals the displayed total.
- The test passes on a fresh run.

### Task 3 — Multiple cart state transitions
#### Scenario
A shopper builds a multi-line cart, removes one line, then removes the last line. The cart must reflect **each transition** correctly and end in a true empty state with the badge reset.
#### Preconditions
A `logged_in_page` (reuse the fixture) OR a plain `page`; the cart empty at the start. You will end at the empty cart.
#### Steps
1. Put **two line items** in the cart — either two different products, or the same product added so the cart holds a quantity of two across lines (whichever your Page Objects support cleanly).
2. Open the cart and record the number of line-item rows and the header badge value.
3. **Remove one line.** Verify the remaining state.
4. **Remove the final line.** Verify the empty-cart state.
#### Expected Results (automate as plain asserts)
- After building the cart, the row count / badge reflects **two** items.
- After removing one line, exactly the expected remaining line stays (row count decreased by one; the surviving product is the one you did **not** remove).
- After removing the final line, the empty-cart message `Ваш кошик порожній!` is visible.
- After the cart is empty, the header badge `#cart` is reset (shows `0` / empty text).
#### Implementation Notes
Reuse `CartPage.remove_first_item()` (or a remove-by-index/-name action if you add two different products). Read state **before and after** each removal and compare — this is a before/after regression, so assert the transition, not just the final screen. Reuse `logged_in_page` and/or `cart_with_product` where they reduce setup. Confirm the remove-button and empty-message selectors, and the reset badge text, in DevTools.
#### Done When
- The test drives the cart through add-two → remove-one → remove-last.
- It asserts the intermediate remaining state (correct row count and surviving product) and the final empty state (`Ваш кошик порожній!` + badge reset).
- `conftest.py` contains both `logged_in_page` and `cart_with_product` fixtures (no `fixtures/` directory) and at least one Lesson 08 test consumes a fixture.
- The tests pass on a fresh run.

## Expected Project Structure After This Lesson
```text
opencart-qa-automation/
├── config.py
├── conftest.py                 # now contains logged_in_page + cart_with_product
├── pytest.ini
├── requirements.txt
├── .gitignore
├── README.md
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── category_page.py
│   ├── product_page.py         # extended: add_to_cart()
│   ├── search_results_page.py
│   ├── register_page.py
│   ├── login_page.py
│   ├── account_page.py
│   └── cart_page.py            # new this lesson (+ parse_price helper)
├── utils/
│   └── data.py                 # unique_email() + generate_user_data(), reused
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    ├── test_locators.py
    ├── test_assertions.py
    ├── test_search.py
    ├── test_registration.py
    ├── test_login.py
    └── test_cart.py            # new this lesson
```

## Git Workflow Reminder
Work on branch `lesson-08`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Extend `ProductPage` with an `add_to_cart()` action and verify the `.alert-success` confirmation plus the `#cart` header badge with plain `assert`.
- Build a `CartPage(BasePage)` in canonical style and assert cart contents by reading the actual product name and quantity (no hard-coded product name).
- Parse displayed prices and **derive** an expected total in the test, then compare it against the store's displayed total instead of hard-coding an amount.
- Drive the cart through multiple state transitions (add → remove one → remove last) and assert each before/after change, ending at `Ваш кошик порожній!` with the badge reset.
- Write and reuse **state-building fixtures** in `conftest.py` — a self-contained `logged_in_page` and a `cart_with_product` — built from `generate_user_data()` + `RegisterPage.register(user)`.
