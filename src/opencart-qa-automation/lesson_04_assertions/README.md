# Lesson 04: Assertions

## Goal
A test is only as good as the questions its assertions ask. You already know how to write `assert` in pytest; this lesson is about **assertion design** — checking the *right* things, in a *readable* way, without pinning your tests to the store's volatile demo data. You will verify a product page's structural contract, prove that data stays consistent as you move between pages, and derive an expected cart state from what the page actually shows instead of hardcoding it. Every check is a plain Python `assert` run by pytest — no Playwright `expect()`.

## Theory
- **An assertion answers a business question.** "Is the price shown in a currency format?" and "Did adding one item raise the cart count by one?" are questions a user cares about. `assert True` and padding checks to inflate a count answer nothing.
- **Assertions live in the TEST, never in a Page Object.** Page Objects expose locators, navigation, and actions. The scenario's `assert` statements stay in the test so a reader sees exactly what is being verified.
- **Assert on structure, format, and derived state — not on volatile values.** The demo store's prices, names, and counts change over time. A test that hardcodes `"$110.00"` or `count == 4` is brittle by design. Instead: check that a price **matches a currency format** (regex), that a name is **non-empty**, that a default quantity **equals the value the field actually carries**, and that a cart total **changed by the amount your action should have caused**.
- **Derive expected values; read before you act.** Capture the "before" state, perform the action, then compare against a value you *computed* from the before state — not a magic number you typed once.
- **Make failures readable.** A bare `assert cond` reports only `AssertionError`. Add a message that shows the actual value: `assert price_re.search(text), f"Unexpected price format: {text!r}"`.

## New Concepts
- **`locator.input_value()`** — reads the current value of an `<input>` (e.g. the default quantity `"1"`), which `inner_text()` cannot see. Use it to assert a field's default.
- **Format assertions with `re`** — `re.compile(r"...")` plus `.search(text)` verifies the *shape* of a string (a currency price) instead of a specific amount.
- **Deriving an expected value** — read a number from the page, compute what it should become, then assert on the computed value (`assert after == before + 1`).
- **Reading state before an action** — call `.inner_text()` / `.input_value()` *before* clicking so you have a baseline to compare against.
- **Uniqueness checks on a collection** — pull several texts (e.g. tab labels), then assert they are the expected set and contain no duplicates (`len(set(labels)) == len(labels)`).

## Practical Explanation
Assertions are ordinary Python. Import `re` only when you check a format. Page Objects hold the locators; the test does the checking.

### Read an input's default value
`inner_text()` returns nothing for an `<input>` — its content lives in the `value` attribute. Use `input_value()`:

```python
qty = product_page.quantity_input.input_value()   # e.g. "1"
assert qty.strip() != "", "Quantity field has no default value"
assert int(qty) >= 1, f"Unexpected default quantity: {qty!r}"
```

### Assert on FORMAT, not on a value
Prices change; their *shape* does not. Match a currency symbol followed by digits:

```python
import re

PRICE_RE = re.compile(r"[$€£]\s?\d[\d.,]*")        # matches "$110.00", "€ 80,00"
price_text = product_page.price.inner_text()
assert PRICE_RE.search(price_text), f"Unexpected price format: {price_text!r}"
```

### Derive an expected value instead of hardcoding it
Read the "before" state, act, then compare against a computed value:

```python
before = cart_page.item_count()          # e.g. 0
product_page.add_to_cart()
after = cart_page.item_count()
assert after == before + 1, f"Cart went from {before} to {after}, expected +1"
```

If `before` is `0` you still never wrote `1` as a literal expectation — you derived `before + 1`. When the demo data changes, the test still holds.

### Keep assertions in the test; keep locators in the Page Object
`ProductPage` follows the same canonical style as every other page — inherit `BasePage`, `super().__init__(page)` first, all locators in `__init__`, a no-arg `open()`:

```python
class ProductPage(BasePage):
    PATH = "desktops/test"                 # Apple Cinema 30

    def __init__(self, page):
        super().__init__(page)
        self.name = page.locator("h1")
        self.price = page.locator(".price")                 # confirm in DevTools
        self.quantity_input = page.locator("input[name='quantity']")
        self.add_to_cart_button = page.locator("#button-cart")
        self.tabs = page.locator("ul.nav-tabs > li")        # one locator per tab item

    def open(self):
        super().open(self.PATH)

def test_add_to_cart_enabled(page):
    product_page = ProductPage(page)
    product_page.open()
    assert product_page.add_to_cart_button.is_enabled()     # the check stays in the test
```

## Homework
Extend the framework — reuse `BasePage`, the `page` fixture from `conftest.py`, and `config` from earlier lessons. Write your tests in `tests/test_assertions.py`. **Do not hardcode volatile prices, product names, or counts** — assert on structure, format, and derived state. Every assertion is a plain `assert`; there is no `expect()` anywhere in this lesson.

### Task 1 — Product-page structural contract
#### Scenario
Before a customer can buy anything, the product page must present a complete, well-formed buying surface: a real name, a properly formatted price, a usable quantity field defaulted to a sensible value, an enabled Add-to-Cart button, and the expected set of information tabs. This task verifies that structural contract without depending on *which* product it is or what it costs today.
#### Preconditions
Being on the Apple Cinema 30 product page (`/desktops/test`).
#### Steps
1. Open the product page via a `ProductPage`.
2. Read the H1 product name.
3. Read the displayed price.
4. Read the quantity field's default value.
5. Read the three tab labels (Опис / Специфікація / Відгуки).
#### Expected Results
- The product name (H1) is present and non-empty after stripping whitespace.
- The price matches a currency **format** via a `re.compile(...)` regex — never a specific amount.
- The quantity default read with `input_value()` is non-empty and parses to an integer `>= 1`.
- The Add-to-Cart button (`#button-cart`) reports `is_enabled()`.
- Exactly three tab labels are present, they match the expected set (`Опис`, `Специфікація`, `Відгуки` — note Reviews shows a count like `Відгуки (0)`, so match by substring), and there are no duplicate labels.
#### Implementation Notes
Create `pages/product_page.py` with `ProductPage(BasePage)` in the canonical style (`PATH = "desktops/test"`, no-arg `open()`, all locators in `__init__`). Use `input_value()` for the quantity default (`inner_text()` will not read an input). Keep all five checks as plain `assert`s in the test — the Page Object holds only locators and `open()`.
#### Done When
- `ProductPage(BasePage)` exists and opens the product via `open()`.
- Name is asserted non-empty (structure, not a hardcoded string).
- Price is asserted against a currency-format regex.
- Quantity default is validated via `input_value()`.
- Add-to-Cart is asserted enabled and the three tabs are validated for expected labels + uniqueness.
- **DevTools:** you confirmed the H1, price element, `input[name='quantity']`, `#button-cart`, and tab (`ul.nav-tabs`) selectors yourself.

### Task 2 — Cross-page data consistency
#### Scenario
A category card promises a product; opening it must deliver the *same* product. If the card shows one name and price but the product page shows another, the store is lying to the customer. This task reads a card's data first, then proves the product page it links to is consistent with it.
#### Preconditions
Being on the Desktops category page (`/desktops`), which lists product cards (`.product-thumb`).
#### Steps
1. Open the Desktops category.
2. Dynamically pick one card (e.g. `.first`). Do **not** assume a specific product.
3. **Before clicking**, read that card's product name, its price text, and its name-link `href`.
4. Open the product by clicking the card's name link.
5. Read the product page's H1 name and its price.
#### Expected Results
- The product page H1 name equals the name read from the card (compare stripped text).
- Both the card price and the product-page price match the **same** currency-format regex (validate the representation, not a shared literal value).
- The current `page.url` corresponds to the `href` you captured from the selected card (the route the link promised is the route you landed on).
#### Implementation Notes
Extend `CategoryPage` (from Lesson 03) to expose the first card and scoped child locators (name link, price) so you can read them before navigating. Reuse `ProductPage` from Task 1 to read the destination. Capture the `href` with `get_attribute("href")` before clicking, and compare a stable fragment of it against `page.url` (routes may be absolute vs relative). Keep every comparison in the test.
#### Done When
- The card's name, price, and link are read **before** navigation.
- The product-page name is asserted equal to the card's name (dynamic, not hardcoded).
- Both prices are validated against the same format regex.
- The landed URL is asserted to correspond to the captured `href`.
- **DevTools:** you confirmed the scoped card selectors (name link, price) and the product-page H1/price selectors.

### Task 3 — Derived expected cart state
#### Scenario
Adding a product to the cart must change the cart by exactly what the action implies — no more, no less. This is the end-to-end payoff of assertion design: instead of hardcoding "the cart should show 1", you read the cart's state before, compute what it should become, and verify the store agrees.
#### Preconditions
A fresh browser session on the Desktops category (an empty or known starting cart state — do not assume it is empty, read it).
#### Steps
1. Open the category and read the header cart's **initial** item count (`#cart`).
2. Dynamically pick a product card and open its product page.
3. On the product page, read the quantity default with `input_value()` and record it as the quantity you are adding.
4. Click Add-to-Cart and wait for the success feedback (`.alert-success`).
5. Read the header cart's item count **after** the add.
#### Expected Results
- The success alert (`.alert-success`) is visible after adding (the action was accepted).
- The expected new count is **derived**: `expected = initial_count + quantity_added` (where `quantity_added` came from the field, not a literal). The actual after-count equals `expected`.
- The count is never hardcoded — if you read `initial_count` and `quantity_added` from the page, the expectation is computed from them.
#### Implementation Notes
Add a small helper on the Page Object (e.g. `CategoryPage.cart_item_count()` or a header/cart Page Object) that parses the number the header cart displays (`#cart` shows a text like `"1 товар(ів)"` — extract the leading integer with a regex). The helper only *reads and returns* the number; the derivation and the `assert` stay in the test. Reuse `ProductPage` from Task 1. If a `cart_with_product` or `logged_in_page` fixture from `conftest.py` helps you set up a known starting state, use it — but still read the baseline rather than assuming it.
#### Done When
- The initial cart count is read from the page before adding.
- The quantity added is taken from `input_value()`, not a literal.
- The success alert is asserted visible.
- The expected after-count is `initial + quantity_added` (derived) and asserted equal to the actual after-count.
- No cart count literal appears in the assertion.
- **DevTools:** you confirmed the `#cart` header text format and the `.alert-success` selector.

## Expected Project Structure After This Lesson
```text
opencart-qa-automation/
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── .gitignore
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── category_page.py
│   └── product_page.py          # new this lesson
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    ├── test_locators.py
    └── test_assertions.py       # new this lesson
```

## Git Workflow Reminder
Work on branch `lesson-04`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Design assertions that each answer a real business question, written as plain pytest `assert` statements — with no Playwright `expect()`.
- Verify a page's structural contract: non-empty name, currency-**format** price via regex, a default input value read with `input_value()`, an enabled control, and an expected, duplicate-free set of labels.
- Prove data consistency across pages by reading values before navigating and comparing after.
- Derive an expected value (cart count from `initial + quantity`) instead of hardcoding volatile data.
- Keep every assertion in the test and every locator in the Page Object, adding a `ProductPage(BasePage)` in the canonical style.
