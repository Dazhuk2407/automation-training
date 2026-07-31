# Lesson 01: Home Page

## Goal
Lesson 00 already gave you a working toolchain, the project structure, `config.py`, `conftest.py`, `BasePage`, and a green smoke test. From here on you never repeat setup — you write real functional coverage. In this lesson you automate the behaviour of the OpenCart **Home Page**: the Featured product cards, navigating from a card into its product page, and the first slice of the buy journey (home → cart). Everything is verified with plain `assert` statements in the tests; Page Objects only hold locators and actions.

## Theory
- The home page of the demo store shows a **Featured** block of product cards. Each card is a `.product-thumb` that carries a product-name link, a price, and an Add-to-Cart control (`В КОШИК`).
- A **collection of elements** is one locator that matches many nodes. `page.locator(".product-thumb")` is a handle to *all* cards; `.count()` tells you how many, and `.nth(i)` scopes to one. Loop over the count to validate every card.
- **Scoping** matters: to read the name of card `i`, locate the card first (`cards.nth(i)`) and search *inside* it (`card.locator("h4 a")`). This guarantees the name and the price you compare come from the *same* card.
- Read volatile data (name, price) from the UI **before** you click, keep it in a variable, then compare after navigating. Never hardcode product names, prices, or counts — the demo data changes.
- The **header cart** (`#cart`) shows the number of items. Adding a product updates it and raises a success message (`.alert-success`). These are the signals a real user relies on, so they are what you assert.

## New Concepts
- Working with a **locator collection**: `.count()`, `.nth(i)`, and iterating over all matches.
- **Dynamic selection**: choosing a product at runtime instead of hardcoding one, and remembering its name/price in a variable.
- **Price FORMAT validation** with a regular expression instead of asserting an exact amount.
- **Round-trip navigation**: opening a product from a card, confirming identity, then using `page.go_back()` to return home.
- Reading **before/after state** (the cart badge) to prove an action changed the application.

## Practical Explanation
Page Objects expose locators and actions only; the test does all the checking with plain `assert`.

```python
# pages/home_page.py
from pages.base_page import BasePage


class HomePage(BasePage):
    PATH = ""  # store root

    def __init__(self, page):
        super().__init__(page)
        self.featured_cards = page.locator("#content .product-thumb")

    def open(self):
        super().open(self.PATH)

    def card(self, index):
        # a single scoped card; the test reads inside it
        return self.featured_cards.nth(index)
```

Validating a whole collection and a price format, all asserts in the test:

```python
# tests/test_home_page.py
import re

from config import BASE_URL
from pages.home_page import HomePage

PRICE_RE = re.compile(r"\d")  # refine to the store's real price shape in DevTools


def test_home_featured_cards_are_consistent(page):
    home = HomePage(page)
    home.open()

    count = home.featured_cards.count()
    assert count > 0                       # Featured section is populated

    for i in range(count):
        card = home.featured_cards.nth(i)
        name = card.locator("h4 a").inner_text().strip()
        price = card.locator(".price").inner_text().strip()
        assert name                        # non-empty product name
        assert PRICE_RE.search(price)      # price has a valid FORMAT
        assert card.locator("h4 a").get_attribute("href")   # real product link
        assert card.get_by_role("button", name="В КОШИК").is_visible()
```

Reading a value *before* clicking, then comparing *after* navigation:

```python
def test_card_opens_matching_product(page):
    home = HomePage(page)
    home.open()

    card = home.featured_cards.first
    expected_name = card.locator("h4 a").inner_text().strip()

    card.locator("h4 a").click()           # navigate into the product
    assert expected_name in page.locator("h1").inner_text()

    page.go_back()                         # round-trip home
    assert page.url.rstrip("/") == BASE_URL.rstrip("/")
```

> Selectors above are illustrative — confirm the real card, name, price, button, and cart selectors yourself in DevTools. Verifying locators is core QA work, which is exactly why they live in Page Objects where they are easy to fix.

## Homework
Do all three tasks on a branch named `lesson-01`. Keep every assertion in the test files as plain `assert`; keep locators and actions in Page Objects.

### Task 1 — Featured product-card consistency
#### Scenario
A shopper landing on the home page must see a real Featured block: every promoted card should show a product they can identify, a readable price, a way to open the product, and a way to add it to the cart. This verifies the home page never renders broken or half-populated cards.
#### Preconditions
On the OpenCart home page (`HomePage.open()`), no login required.
#### Steps
1. Open the home page.
2. Locate the collection of Featured cards.
3. Read the number of cards and iterate over every one of them.
4. For each card, read its name text, its price text, its product-link `href`, and locate its Add-to-Cart control.
#### Expected Results
- The Featured section is populated: card `count()` is greater than 0.
- Every card has a non-empty product name (`inner_text().strip()` is truthy).
- Every card's price matches a valid price FORMAT (use a regex; do NOT assert an exact amount).
- Every card exposes a non-empty product link `href` and a visible Add-to-Cart control.
#### Implementation Notes
Give `HomePage` a locator for the Featured card collection (`.product-thumb` scoped to the content area). Read each card by scoping inside `nth(i)` — do not use separate, page-wide locators for names and prices, or they may drift out of alignment. Loop with `range(count)`. Define the price regex in the test. No new Page Object is required beyond extending `HomePage`.
#### Done When
- `test_home_featured_cards_are_consistent` iterates over all cards (not just the first).
- Name, price-format, link, and Add-to-Cart checks all pass for every card.
- No product name, price, or count is hardcoded.
- The test is green.

### Task 2 — Product navigation consistency
#### Scenario
Clicking a product card must take the shopper to *that* product — not a different one, not a broken page — and the browser Back button must bring them cleanly home to keep browsing. This verifies card-to-product navigation is trustworthy in both directions.
#### Preconditions
On the home page with a populated Featured block.
#### Steps
1. Open the home page.
2. Dynamically select one displayed product card (e.g. the first, or a computed index).
3. Read and remember that card's product name **before** clicking.
4. Click the card's product link to open the product page.
5. Read the product page's heading/title.
6. Use the browser Back button to return to the home page.
#### Expected Results
- The opened product page corresponds to the selected card: the remembered name appears in the product page's `h1` (or title).
- The product URL is a real product route (its `href`/`page.url` changed away from the home URL).
- After Back, `page.url` is the home page again and the Featured block is present once more.
#### Implementation Notes
Do NOT hardcode a product name — capture it from the card at runtime and compare after navigation. Reuse the scoped-card approach from Task 1 to read the name. Use `page.go_back()` for the return trip; assert on `page.url` against `BASE_URL` (from `config`). You may introduce a lightweight `ProductPage` for the `h1` locator, or read the heading directly in the test — either is acceptable as long as assertions stay in the test.
#### Done When
- `test_card_opens_matching_product` selects a card dynamically and remembers its name before clicking.
- The product page identity matches the selected card's name.
- Browser Back returns to the home page (asserted on `page.url`).
- No hardcoded product name or route; the test is green.

### Task 3 — Home-to-cart user journey
#### Scenario
The core of an e-commerce store is adding a product to the cart. A shopper picks a product, adds it, sees confirmation, watches the cart counter go up, opens the cart, and finds exactly the product they chose. This end-to-end slice verifies the first real purchase step works and is reflected consistently across the success message, the header badge, and the cart page.
#### Preconditions
On the home page with an empty cart (fresh browser context — the `page` fixture gives one per test).
#### Steps
1. Open the home page.
2. Dynamically choose a product and remember its name (from its card, or from its product page after opening it).
3. Read the current cart badge count (the before-state).
4. Add the chosen product to the cart (from the card's Add-to-Cart control, or from the product page's `#button-cart`).
5. Wait for the success feedback.
6. Read the cart badge count again (the after-state).
7. Open the cart page.
#### Expected Results
- A success message appears after adding (`.alert-success` is visible).
- The cart badge count **changed**: derive the expected value from the before-state (before + 1), do NOT hardcode the number.
- The cart page opens on the cart route with the cart title.
- The cart page contains the remembered product name (the same product that was added).
#### Implementation Notes
Add an Add-to-Cart action to `HomePage` (or `ProductPage`) and a header-cart open action; introduce a small `CartPage` exposing a locator for cart line items and the cart-open control (header `#cart`). Capture the product name and the initial badge count as variables in the test and compute the expected new count there — deriving expected state instead of hardcoding is the point of this task. Assertions (success visible, count delta, product present) all live in the test. This is the hardest task: it spans multiple pages and before/after state, so build it after Tasks 1 and 2.
#### Done When
- `test_home_to_cart_journey` chooses a product dynamically and remembers its name.
- Success feedback, a derived cart-count change, and the product's presence on the cart page are all asserted.
- No hardcoded product name, price, or cart count.
- The test is green.

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
│   ├── home_page.py        # extended: Featured cards, add-to-cart, open-cart
│   ├── product_page.py     # optional: product heading + #button-cart
│   └── cart_page.py        # new: cart line items + open control
└── tests/
    ├── test_smoke.py
    └── test_home_page.py   # new this lesson (3 functional tests)
```

## Git Workflow Reminder
Work on branch `lesson-01`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Validate an entire collection of UI elements by iterating with `.count()` and `.nth(i)`, scoping reads to the correct card.
- Select data dynamically and validate price FORMAT with a regex instead of hardcoding volatile demo values.
- Verify card-to-product navigation and a clean browser-Back round trip.
- Automate a home-to-cart journey, asserting success feedback, a derived cart-count change, and product presence on the cart page.
- Keep every assertion in the test as a plain `assert`, with locators and actions confined to Page Objects.
