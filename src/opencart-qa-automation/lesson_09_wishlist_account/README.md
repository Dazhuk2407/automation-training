# Lesson 09: Wishlist & Account

## Goal
Continue from Lessons 00–08 and automate an **authentication-gated** feature: the OpenCart **Wish List** (`account/wishlist`). You will prove the wishlist is protected (logged-out access **redirects to Login**), then **reuse the `logged_in_page` fixture from `conftest.py`** to drive real state transitions — add an item, confirm it, add the same item again and observe how duplicates are handled, remove it, and confirm the empty state. Finally you will automate the **wishlist-to-cart** journey: move a wished item into the cart and verify both the cart and the resulting wishlist state. By the end you will have a `WishlistPage`, an extended `ProductPage`, and `tests/test_wishlist.py`.

## Theory
- Some features are **auth-gated**: OpenCart serves the wishlist only to a logged-in customer. Opening `account/wishlist` while logged out **redirects to the Login page** (route `account/login`, title `Авторизація`). Asserting that redirect is a real, valuable test that needs no login at all.
- Once logged in, an item is added from a **product page** via an "Add to Wish List" control; OpenCart answers with a green **success alert** (`.alert-success`). The wishlist page then **lists items** in rows, each with an add-to-cart control and a remove control.
- **Duplicate handling is a real business rule.** Adding the *same* product to the wishlist twice does not silently create two identical rows in most store versions — OpenCart typically reports it is already there (or keeps a single row). The interesting test is asserting the **actual, observed** behaviour, not assuming it.
- **All shared fixtures live in `conftest.py`.** `logged_in_page` (introduced in Lesson 08) registers a fresh unique user — which auto-authenticates — and yields an already-authenticated `page`. Reuse it: no login boilerplate in this lesson's tests.
- Moving an item from the wishlist to the cart is a **cross-feature state change**: it should populate the cart while leaving the wishlist in a defined state. Verifying both sides is what makes it an end-to-end check.

## New Concepts
- Testing an **auth-gated** feature by asserting a **redirect to Login** when accessed while logged out, then confirming the **same route becomes reachable** once authenticated.
- Reusing the `logged_in_page` fixture instead of repeating login per test.
- **State transitions on a collection**: add → confirm count/name → add duplicate → assert duplicate handling → remove → assert empty state.
- A **cross-feature journey**: moving a wishlist item into the cart and asserting state on *both* pages.

## Practical Explanation
Canonical Page Object style, as all course long: inherit `BasePage`, call `super().__init__(page)` first, define **all locators in `__init__`**, expose only actions, and open with a no-arg `open()` built on a `PATH` constant. **Assertions live only in the tests, as plain `assert` statements — no `expect()`.** Selectors below are **illustrative**; confirm the real ones in DevTools.

### 1. An auth-gate check needs no login
Drive the ordinary logged-out `page` through `WishlistPage` and assert OpenCart bounced you to Login.

```python
# tests/test_wishlist.py  (illustrative pattern — not the homework solution)
from pages.wishlist_page import WishlistPage


def test_wishlist_redirects_anonymous_user(page):
    wishlist = WishlistPage(page)
    wishlist.open()                                  # logged out -> redirected to Login
    assert "account/login" in page.url
    assert "Авторизація" in page.title()
```

### 2. A small `WishlistPage(BasePage)`
A `PATH` constant, a no-arg `open()`, and read-back helpers the test asserts on.

```python
# pages/wishlist_page.py
from pages.base_page import BasePage


class WishlistPage(BasePage):
    PATH = "index.php?route=account/wishlist"

    def __init__(self, page):
        super().__init__(page)
        self.rows = page.locator("#content table tbody tr")   # one row per item
        self.success_alert = page.locator(".alert-success")
        # EXAMPLE controls — confirm the real per-row buttons in DevTools:
        self.add_to_cart_buttons = page.locator("button[data-original-title='Додати в кошик']")
        self.remove_buttons = page.locator("a[data-original-title='Видалити']")
        # EXAMPLE empty-state text — confirm the exact wording in DevTools:
        self.empty_message = page.get_by_text("Список бажань порожній")

    def open(self):
        super().open(self.PATH)

    def item_count(self):
        return self.rows.count()

    def add_first_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def remove_first(self):
        self.remove_buttons.first.click()
```

### 3. Reuse `logged_in_page` — don't log in again
Ask for the fixture and act on the already-authenticated page. Extend `ProductPage` with an `add_to_wishlist()` action, then read the wishlist back.

```python
# tests/test_wishlist.py
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage


def test_wishlist_adds_item(logged_in_page):
    page = logged_in_page                            # already authenticated — no login code
    product = ProductPage(page)
    product.open()                                   # Apple Cinema 30"
    product_name = product.name.inner_text().strip() # read BEFORE navigating away
    product.add_to_wishlist()
    assert product.success_alert.is_visible()

    wishlist = WishlistPage(page)
    wishlist.open()
    assert wishlist.item_count() == 1
    assert product_name in wishlist.rows.first.inner_text()
```

Add-to-Wishlist lives on `ProductPage` (extend the class you already have):

```python
# pages/product_page.py  (extend your existing class — illustrative)
    # ... existing locators (name/H1, price, tabs, add_to_cart_button, success_alert) ...
    # EXAMPLE selector — confirm the real Add-to-Wish-List control in DevTools:
    self.wishlist_button = page.locator("button[data-original-title='Додати в список бажань']")

def add_to_wishlist(self):
    self.wishlist_button.click()                     # -> green success alert appears
```

> Routes stay stable, but the "Add to Wish List" control, the wishlist rows, the per-row add-to-cart and remove controls, and the empty-wishlist text can differ by store version and UI language. Open each page in DevTools (right-click → Inspect) and **confirm the real selectors and text** — the values marked EXAMPLE are starting points, not guarantees.

## Homework
Do all three tasks on a branch named `lesson-09`. Use **plain `assert`** only (no `expect()`); keep every assertion in the test files.

### Task 1 — Wishlist authorization gate
#### Scenario
The wishlist is private to a logged-in customer. A guest who tries to open it must be sent to Login; after authenticating, that exact same route must become reachable. This verifies the access-control boundary from both sides.
#### Preconditions
- A logged-out browser session (the plain `page` fixture) for the guest half.
- The `logged_in_page` fixture from `conftest.py` for the authenticated half (a fresh registered, auto-authenticated user).
#### Steps
1. With the logged-out `page`, create `WishlistPage` and call `open()`.
2. Observe where OpenCart lands you.
3. In a separate test using `logged_in_page`, open `WishlistPage` again on the authenticated page.
4. Observe the resulting route and page identity.
#### Expected Results
- Logged out: the URL contains `account/login` and the title contains `Авторизація` (the guest was redirected — the wishlist did **not** render).
- Logged in: the URL contains `account/wishlist` (you stayed on the wishlist, no redirect) and the wishlist container/heading is visible.
#### Implementation Notes
Create `pages/wishlist_page.py` with `WishlistPage(BasePage)` (canonical `PATH` + no-arg `open()`, locators in `__init__`). Reuse the existing `logged_in_page` fixture — do not write any register/login code. Two separate tests (guest and authenticated) keep the boundary clear.
#### Done When
- `WishlistPage(BasePage)` opens `account/wishlist` via `open()`.
- One test asserts the logged-out redirect to Login (URL + title).
- One test asserts the authenticated user stays on `account/wishlist`.
- You confirmed the redirect and the real wishlist container in DevTools.

### Task 2 — Wishlist state transitions and duplicate handling
#### Scenario
A customer curates a wishlist: they add a product, see it listed, try to add the very same product again, then remove it. This verifies the collection behaves correctly through add → duplicate → remove, ending in a clean empty state.
#### Preconditions
- The `logged_in_page` fixture (authenticated user, empty wishlist).
- `ProductPage` extended with an `add_to_wishlist()` action.
#### Steps
1. Open the product page and **read the product name before navigating away**.
2. Call `add_to_wishlist()`; confirm the success feedback.
3. Open `WishlistPage`; confirm exactly one row and that it shows the saved product name.
4. Return to the product page and call `add_to_wishlist()` **again** for the same product.
5. Reopen `WishlistPage` and inspect the row count / the message OpenCart returned.
6. Remove the item from the wishlist.
7. Reopen (or observe) the wishlist and confirm the empty state.
#### Expected Results
- After the first add: `.alert-success` is visible; the wishlist has exactly one row whose text contains the saved product name.
- After the duplicate add: assert the **actually observed** behaviour — the wishlist still shows a single row for that product (no duplicate line was created). Confirm the real outcome in DevTools and assert on that (row count stays 1 for the product).
- After removal: the wishlist shows its empty-state message (e.g. `Список бажань порожній`) and/or the item count is 0.
#### Implementation Notes
Extend `ProductPage` with the Add-to-Wishlist locator in `__init__` and an `add_to_wishlist()` action; add `item_count()` and `remove_first()` helpers to `WishlistPage`. Reuse `logged_in_page` — no login boilerplate. Read the product name dynamically instead of hardcoding it; derive the expected row count from the observed behaviour rather than assuming duplicates are or aren't allowed.
#### Done When
- The test uses `logged_in_page` and repeats no login code.
- Add is asserted (success alert + one row containing the product name).
- The duplicate-add outcome is asserted against the real observed behaviour (single row for the product).
- Removal is asserted to produce the empty-wishlist state (message and/or count 0).
- You confirmed the Add-to-Wishlist control, the wishlist rows, the remove control, and the empty-state text in DevTools.

### Task 3 — Wishlist-to-cart journey
#### Scenario
A shopper moves a saved product from the wishlist into the cart. The action must populate the cart with the correct product and leave the wishlist in a defined, verified state. This is a cross-feature end-to-end flow spanning the product page, the wishlist, and the cart.
#### Preconditions
- The `logged_in_page` fixture (authenticated user, empty wishlist and empty cart).
- `ProductPage.add_to_wishlist()` (Task 2) and the existing `CartPage` from Lesson 08.
#### Steps
1. Open the product page; **read the product name** before leaving.
2. Add the product to the wishlist and confirm it appears (one row with the name).
3. On the wishlist, use the row's **add-to-cart** control to move the product into the cart.
4. Open `CartPage` and inspect the line items.
5. Reopen (or observe) `WishlistPage` and inspect its resulting state.
#### Expected Results
- The cart contains a line whose text includes the saved product name (the same product that was wished).
- The header cart badge (`#cart`) reflects the added item.
- The wishlist's state after the move is asserted against the **actually observed** behaviour — in OpenCart the item typically remains in the wishlist after adding it to the cart. Confirm the real outcome in DevTools and assert on it (e.g. the row is still present, or the empty state, whichever the store actually shows).
#### Implementation Notes
Reuse `logged_in_page`, the extended `ProductPage`, the `WishlistPage` (add an `add_first_to_cart()` helper), and the Lesson 08 `CartPage`. Do not duplicate cart-page logic — import and reuse `CartPage`. Read the product name once and compare it on the cart page; do not hardcode volatile data. The cross-feature value is in asserting **both** the cart side and the wishlist side after a single action.
#### Done When
- The test uses `logged_in_page` and reuses `ProductPage`, `WishlistPage`, and `CartPage` (no duplicated setup).
- The cart is asserted to contain a line with the saved product name, and the `#cart` badge reflects it.
- The post-move wishlist state is asserted against the real observed behaviour.
- You confirmed the wishlist row's add-to-cart control and the cart line-item selector in DevTools.

## Expected Project Structure After This Lesson
```text
opencart-qa-automation/
├── config.py
├── conftest.py               # holds logged_in_page + cart_with_product (from Lesson 08)
├── pytest.ini
├── requirements.txt
├── .gitignore
├── README.md
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── category_page.py
│   ├── product_page.py       # extended: add_to_wishlist()
│   ├── search_results_page.py
│   ├── register_page.py
│   ├── login_page.py
│   ├── account_page.py
│   ├── cart_page.py
│   └── wishlist_page.py      # new this lesson
├── utils/
│   └── data.py
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    ├── test_locators.py
    ├── test_assertions.py
    ├── test_search.py
    ├── test_registration.py
    ├── test_login.py
    ├── test_cart.py
    └── test_wishlist.py      # new this lesson
```

## Git Workflow Reminder
Work on branch `lesson-09`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Verify an **auth-gated** feature from both sides: a logged-out redirect to Login and the same route becoming reachable once authenticated.
- **Reuse** the `logged_in_page` fixture from `conftest.py` to write short, focused tests without repeating login code.
- Drive a full **collection state transition** — add, confirm, duplicate, remove — and assert the real empty state.
- Automate a **cross-feature wishlist-to-cart journey**, asserting state on both the cart and the wishlist.
- Write every assertion as a plain `assert` in the test, and confirm real selectors and text in DevTools instead of trusting example values.
