# Lesson 03: Locators

## Goal
This lesson continues from Lesson 02, reusing your `BasePage`, `HomePage`, `config.py`, and the `page` fixture. A test is only as reliable as the locators it uses to find elements. Here you learn to choose **robust** Playwright locators — preferring role, text, and label strategies over fragile CSS — and, more importantly, to **scope** a locator inside a parent element so you can read one field of one specific product card. Locators are the learning tool; the work is functional: you will validate a whole category of cards, compare two cards without cross-contamination, and find a product by its content rather than its position. You will **extend** the `CategoryPage` you introduced in Lesson 02 — giving it a direct `open()` and a content-filter helper — and write `tests/test_locators.py`, keeping every locator inside the Page Object and every assertion inside the test.

## Theory
- A **locator** is Playwright's lazy handle to an element (or a set of elements). It is re-resolved on every action, so it stays valid as the page updates — you build it once in `__init__` and reuse it.
- **Robust vs brittle:** locators tied to *what the user sees* (an element's role and accessible name, its visible text, or a field's label) survive redesigns. Deep CSS paths, auto-generated class names, and exact DOM nesting break as soon as the markup shifts.
- **Order of preference** (top = most robust): `get_by_role`, then a stable `locator("<css>")` hook, then `get_by_text`, `get_by_label`, `get_by_placeholder`. Reach for CSS only when the markup gives a clean, meaningful attribute (`input[name='search']`, `.product-thumb`) — not a brittle chain of nested tags.
- **One locator can match many elements.** A collection like `.product-thumb` resolves to every card on the page; you count them with `.count()` and address one with `.nth(i)`.
- **Scoping is the core skill.** Call `.locator(...)` (or a `get_by_*` method) **on another locator** to search only *inside* that parent. This is how you read the name of one card without matching the name of every card — and how two cards stay independent.
- **Finding by content, not position.** `.first` is convenient but positional: it silently follows whatever the store shows first. To target a *known* product, filter the collection by its text (`.filter(has_text=...)`) so the test still points at the right card after the catalog is reordered.

## New Concepts
- `get_by_role(role, name=...)` — find by accessible role and name; most robust, your first choice.
- `page.locator("<css>")` — a CSS/selector locator for stable, meaningful hooks (`.product-thumb`, `input[name='search']`).
- `get_by_text(...)`, `get_by_label(...)`, `get_by_placeholder(...)` — match by visible text, form label, or placeholder.
- `locator.count()` — how many elements a collection matched (a plain `int`).
- `locator.nth(i)` / `locator.first` — narrow a multi-match locator down to a single element.
- **Scoping** a child locator inside a parent locator (`card.locator(...)`, `card.get_by_role(...)`).
- `locator.filter(has_text=...)` — narrow a collection to the element(s) that contain given text: find a card by *content*, not by index.
- `locator.all()` — materialise a collection into a list of per-element locators you can loop over.

## Practical Explanation
The site UI is Ukrainian — quote labels from the real interface, and always confirm a selector in DevTools (right-click → Inspect) before trusting it.

### Robust vs brittle
```python
# Brittle: tied to layout / generated structure
search_input = page.locator("div.container div#search input")
# Robust: tied to a stable, meaningful attribute
search_input = page.locator("input[name='search']")

# Brittle: a class chain
login_button = page.locator("form .buttons input.btn-primary")
# Robust: role + visible name (Ukrainian label = "Вхід")
login_button = page.get_by_role("button", name="Вхід")
```

### A collection, then scoping into ONE card
A collection locator matches many elements. Count them, address one, then scope child locators *inside* that card so each read comes from that card only:

```python
cards = page.locator(".product-thumb")   # the whole collection
count = cards.count()                     # how many cards on the page

card = cards.nth(0)                        # one specific card
name = card.get_by_role("link").first     # searched INSIDE this card
price = card.locator(".price")            # this card's price element
add_button = card.get_by_role("button", name="В КОШИК")
```

`card.locator(...)` searches only within that one card — the same selector run against the whole page would match every card. That difference is the whole point of scoping.

### Looping every card with `.all()`
`.all()` turns the collection into a list of per-card locators you can iterate:

```python
for card in page.locator(".product-thumb").all():
    name = card.get_by_role("link").first.inner_text().strip()
    ...
```

### Finding a card by its content
`.first`/`.nth(i)` are positional. To point at a *named* product regardless of order, filter by text:

```python
target = page.locator(".product-thumb").filter(has_text="Apple Cinema")
```

`target` is still a card locator, so you keep scoping inside it (`target.get_by_role("button", ...)`).

### The test does the asserting — with plain `assert`
Page Objects expose elements and actions; the **test** asserts with ordinary pytest `assert` statements (no `expect()` in this course):

```python
# tests/test_locators.py
from pages.category_page import CategoryPage


def test_category_has_products(page):
    category_page = CategoryPage(page)
    category_page.open()
    assert category_page.products.count() > 0
    first_name = category_page.products.nth(0).get_by_role("link").first.inner_text()
    assert first_name.strip()   # non-empty name
```

`CategoryPage` already exists from Lesson 02 (its `heading`, `breadcrumb`, and `products` collection locator). Here you **extend** it in the course-wide style — add a `PATH` and a no-arg `open()` so the category can be opened directly, and a `card_by_text()` helper. The `.product-thumb` collection stays the same `self.products` locator; do not duplicate it:

```python
# pages/category_page.py  (extended from Lesson 02)
from pages.base_page import BasePage


class CategoryPage(BasePage):
    PATH = "desktops"   # Настільні комп'ютери

    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator("h1")                 # from Lesson 02
        self.breadcrumb = page.locator("ul.breadcrumb")   # from Lesson 02
        self.products = page.locator(".product-thumb")    # the product-card collection

    def open(self):
        super().open(self.PATH)                           # NEW: direct navigation

    def card_by_text(self, text):
        # NEW: find a card by its content, not its position
        return self.products.filter(has_text=text)
```

## Homework
Reuse `BasePage`, the `page` fixture from `conftest.py`, and `config` from earlier lessons — extend, don't rebuild. Every locator lives in a Page Object; every assertion lives in a test as a plain `assert` (no `expect()`). Do not hardcode product counts, prices, positions, or names except where a task names a known stable product.

### Task 1 — Validate every card in a category
#### Scenario
A shopper browsing the **Desktops** category expects each product card to be complete and usable: it must show a name, link to a product, display a price, and offer an Add-to-Cart control. This verifies the category listing is not silently broken for any card.
#### Preconditions
- The framework from Lesson 02 is in place (`BasePage`, `HomePage`, `page` fixture, `config`).
- You are able to open the Desktops category (`/desktops`, heading `Настільні комп'ютери`).
#### Steps
1. Open the Desktops category through `CategoryPage.open()`.
2. Read the product-card collection (`.product-thumb`) and confirm it is non-empty.
3. Loop over **every** card (use `.all()` or index with `.nth(i)` up to `count()`).
4. For each card, scope child locators *inside that card* to read its name link, price, and Add-to-Cart control.
#### Expected Results
- The category has at least one card (`products.count() > 0`).
- For **every** card: its name text is non-empty (`inner_text().strip()`).
- For **every** card: its product link has a non-empty, valid `href` (an actual product URL, not `#` or empty).
- For **every** card: its price text matches a currency **format** via regex (symbol + digits), never a specific amount.
- For **every** card: its Add-to-Cart control (`В КОШИК`) is present and visible.
#### Implementation Notes
- Extend the existing `pages/category_page.py` (from Lesson 02): keep `CategoryPage(BasePage)` in the canonical style and add a `PATH = "desktops"` plus a no-arg `open()` that calls `super().open(self.PATH)`. Reuse its existing `.product-thumb` collection locator `self.products` — do not add a second collection locator.
- New concepts to apply: `locator.count()`, `locator.all()`, and **scoping** child locators inside each card (`card.get_by_role("link").first`, `card.locator(".price")`, `card.get_by_role("button", name="В КОШИК")`).
- Read the `href` with `card.get_by_role("link").first.get_attribute("href")`.
- A reusable price-format regex, e.g. `re.compile(r"[$€£]\s?\d[\d.,]*")` — assert the shape, not a value.
- Keep all four checks in the loop inside the test; the Page Object only exposes `self.products`.
#### Done When
- `CategoryPage(BasePage)` is extended with a `PATH`, a no-arg `open()`, and reuses its `.product-thumb` collection locator (`self.products`).
- `test_category_all_cards_valid` loops every card and asserts non-empty name, valid `href`, price format, and a visible Add-to-Cart per card.
- No assertion depends on a hardcoded count, name, or price value.
- You confirmed the card selector and its child selectors (name link, `.price`, `В КОШИК`) in DevTools.
- The test passes.

### Task 2 — Compare two scoped cards
#### Scenario
When a test reads "the price" or "the name" of a product, it must be certain the value came from the *intended* card and not leaked from a neighbour. This proves your scoped locators isolate one card from another, then follows one card through to its product page.
#### Preconditions
- Task 1 complete: `CategoryPage` opens Desktops and exposes the `.product-thumb` collection.
- The Desktops category shows at least two different cards.
#### Steps
1. Open the Desktops category.
2. Select **two different** cards by index (`products.nth(0)` and `products.nth(1)`).
3. From each card, scope its name link and its product `href` — reading each value from that card only.
4. Click the name link of the **first** card to open its product page.
5. Read the product page's H1 name.
#### Expected Results
- Both selected cards have non-empty names (each read via its own scoped locator).
- The two names are **different** from each other (proving the scopes did not both resolve to the same card).
- The two product `href` values are **different** from each other.
- After opening the first card, the product page's H1 **corresponds to that card's name** — the name captured before the click matches (allow for trailing punctuation such as `"` in the H1).
#### Implementation Notes
- Reuse `CategoryPage`; no new Page Object is required for the cards, though you may reuse a `ProductPage`/H1 read if you have one, or read `page.locator("h1").inner_text()` directly in the test.
- Capture each card's name and `href` into local variables *before* navigating — after a click the category locators no longer point at a live page.
- Compare names/links with plain `assert a != b`. For the H1 match, normalise (e.g. `startswith`, or strip a trailing `"`), since the product H1 may add punctuation the card name omits.
- Address cards with `.nth(0)` / `.nth(1)`; scope with `card.get_by_role("link").first`.
#### Done When
- `test_two_cards_are_independent` selects two cards by index and reads each card's name/`href` through scoped locators.
- It asserts the two names differ and the two `href` values differ.
- It opens the first card and asserts the product H1 corresponds to the name captured from that card.
- Nothing is hardcoded to a specific product; the values come from the page at runtime.
- You confirmed the name-link and H1 selectors in DevTools.
- The test passes.

### Task 3 — Find a product by its content
#### Scenario
A real test targets a *known* product ("add **Apple Cinema 30** to the cart"), not "whatever happens to be first." Positional `.first` silently follows a reordered catalog. This finds a card by its content, acts inside only that card, and proves the action affected the intended product alone.
#### Preconditions
- Tasks 1–2 complete: `CategoryPage` opens Desktops and exposes the `.product-thumb` collection.
- The Desktops category contains a stable, known product — use **Apple Cinema 30** (`/desktops/test`), the one product this course treats as fixed.
#### Steps
1. Open the Desktops category.
2. Find the card whose content matches the target product name using `.filter(has_text=...)` — **do not** rely on `.first`/`.nth`.
3. Read and remember that card's name before acting.
4. Scope the Add-to-Cart control (`В КОШИК`) *inside the matched card* and click it.
5. Observe the resulting application state (success alert `.alert-success`, header cart `#cart`).
#### Expected Results
- `.filter(has_text=...)` resolves to exactly **one** card (`filtered.count() == 1`), confirming the content match is unambiguous.
- The matched card's scoped name contains the target text (you targeted the right product).
- After clicking Add-to-Cart inside that card, a success confirmation appears (`.alert-success` is visible) and its text references the selected product name.
- The header cart (`#cart`) reflects the change (its text is non-empty / shows the added item) — the state that changed corresponds to the **selected** product, not another card.
#### Implementation Notes
- Add a `card_by_text(text)` helper to `CategoryPage` returning `self.products.filter(has_text=text)`; keep it a locator-returning action (no assertions in the Page Object).
- New concept to apply: `locator.filter(has_text=...)` for content-based selection instead of positional `.first`.
- Scope the button on the filtered card: `matched.get_by_role("button", name="В КОШИК")` (confirm role/text in DevTools; it may be a link/button).
- The success alert text on OpenCart names the product (e.g. "Ви додали ... до кошика"); assert the target name is `in` that text rather than matching the full string.
- Add-to-Cart is asynchronous — read the alert/`#cart` *after* the click; Playwright auto-waits when you query the alert locator.
#### Done When
- `CategoryPage.card_by_text(...)` finds a card by content via `.filter(has_text=...)`.
- `test_add_selected_product_to_cart` targets **Apple Cinema 30** by content (not position), asserts exactly one card matched, then adds it to the cart from inside that card.
- It asserts the success alert is visible and references the selected product, and that the header cart state changed accordingly.
- The selection does not use `.first`/`.nth`; no other card's state is asserted to have changed.
- You confirmed the filter match, the scoped `В КОШИК` control, `.alert-success`, and `#cart` in DevTools.
- The test passes.

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
│   └── category_page.py        # extended this lesson: PATH + open() + card_by_text()
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    └── test_locators.py         # NEW this lesson
```

## Git Workflow Reminder
Work on branch `lesson-03`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Choose robust locators in order — `get_by_role`, then a stable `locator("<css>")` hook, then `get_by_text`, `get_by_label`, `get_by_placeholder`.
- Use a collection locator, count matches with `.count()`, loop with `.all()`, and address one element with `.nth(i)`.
- Scope child locators inside a parent card so every read comes from the correct card and two cards stay independent.
- Find a product by its content with `.filter(has_text=...)` instead of relying on positional `.first`.
- Act inside a single scoped card and verify that only the selected product changed application state.
- Extend `CategoryPage(BasePage)` in the canonical style (add a `PATH` + no-arg `open()` and a content-filter helper, all locators in `__init__`) and keep every assertion in the test as a plain `assert`.
