# Lesson 02: Navigation

## Goal
The store is a graph of pages joined by links: the top category menu, the header account/cart links, and nested subcategories. In this lesson you make your framework travel that graph reliably and *prove where it landed* — not by trusting that the URL merely changed, but by reading the destination page's own heading, route, and breadcrumb trail. You extend `HomePage` (and add a small `CategoryPage`) with navigation actions and locators, and you write `tests/test_navigation.py` whose plain `assert` statements confirm real arrival.

## Theory
- A navigation is only "correct" if three independent signals agree: the **route** in `page.url`, the page's **heading** (`h1`), and the **breadcrumb** trail. Checking only `page.url != old_url` proves motion, not destination — a broken link can also change the URL.
- OpenCart main categories use SEO routes (`/desktops`), while nested subcategories often use `index.php?route=product/category&path=...`. Never assume the format — read the real `href` from the link and assert against that.
- The **breadcrumb** (`.breadcrumb`) encodes the hierarchy: `Головна` (Home) → parent → current. It is the cheapest way to confirm you are at the right *level*, and its links let you walk back up.
- `page.go_back()` returns to the previous entry in history; auto-waiting applies, so after it you can immediately re-read the restored page.

## New Concepts
- Reading a destination's identity in the test with the native API: `page.title()`, `page.url`, and `locator.inner_text()` on the `h1`/breadcrumb.
- Deriving expected routes from a link's own `get_attribute("href")` instead of hardcoding volatile URLs.
- **Parametrizing** one navigation test over several categories with `@pytest.mark.parametrize`.
- Walking a hierarchy: top category → subcategory → back up through a breadcrumb link, then confirming the parent page is restored.
- A thin `CategoryPage` Page Object exposing the heading, breadcrumb, and product-grid locators (actions/locators only — assertions stay in tests).

## Practical Explanation
Page Objects expose *locators and actions*; the test reads state and asserts. A category link click, then a plain-assert confirmation of arrival:

```python
# pages/category_page.py
from pages.base_page import BasePage


class CategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator("h1")
        self.breadcrumb = page.locator("ul.breadcrumb")
        self.products = page.locator(".product-thumb")
```

```python
# tests/test_navigation.py (excerpt)
def test_navigation_desktops_category(page):
    home = HomePage(page)
    home.open()
    home.open_category("Настільні комп'ютери")

    category = CategoryPage(page)
    assert category.heading.inner_text().strip() == "Настільні комп'ютери"
    assert "/desktops" in page.url
    assert "Настільні комп'ютери" in category.breadcrumb.inner_text()
    assert category.products.count() > 0   # category content actually loaded
```

Note the four independent signals: heading text, route, breadcrumb, and non-empty content. Any one alone is weak; together they prove correct arrival. Selectors shown here are illustrative — confirm each in DevTools.

## Homework
Do all three tasks on a branch named `lesson-02`. Use plain `assert` only — do **not** import or use `expect()`.

### Task 1 — Main category navigation (parametrized)
#### Scenario
A shopper clicks a top-level category in the main menu and must land on that category's listing page — the right heading, the right route, the right breadcrumb, and actual products on screen.
#### Preconditions
The home page is open (`HomePage.open()`); the main category menu (`#menu`) is visible.
#### Steps
1. Open the home page.
2. Click a top-level category by its visible name.
3. Read the destination heading (`h1`), the breadcrumb text, `page.url`, and the product grid.
#### Expected Results (automate as plain asserts)
- The `h1` heading text equals the expected category name for that row.
- `page.url` contains the expected route fragment for that category.
- The breadcrumb text contains both `Головна` and the category name (Home → category).
- The category listing is populated: `.product-thumb` count is greater than zero.
#### Implementation Notes
Add `HomePage.open_category(name)` that clicks the menu link by visible text within `#menu`. Add a `CategoryPage` with `heading`, `breadcrumb`, and `products` locators. Parametrize the test with `@pytest.mark.parametrize` over at least two categories, each row supplying `(menu_name, expected_route, expected_heading)` — e.g. Desktops → `/desktops` / `Настільні комп'ютери`. Confirm every category name and route in DevTools before committing; do not hardcode product counts.
#### Done When
- `open_category(name)` exists and is used by the test.
- The parametrized test runs at least two categories and asserts heading, route, breadcrumb, and non-empty content for each.
- All parametrized cases pass.

### Task 2 — Header navigation map
#### Scenario
The header links (Register, Login, Wishlist, Cart) form the account/checkout entry points. Each must point somewhere real, reach the correct page, and let the user return — a common regression when a header is refactored.
#### Preconditions
The home page is open. The four header links exist in `HomePage.__init__` (Register `Реєстрація`, Login `Вхід`, Wishlist `Список побажань`, Cart `Кошик`).
#### Steps
1. Open the home page.
2. For each header link: read its `href`, click it, read the destination identity (title / route / heading), then use `page.go_back()` to return home.
#### Expected Results (automate as plain asserts)
- No link is broken: each link's `href` is non-empty and is not just `#` or `javascript:`.
- Each link reaches the correct destination — assert the expected route fragment is in `page.url` **and** the destination page identity matches (e.g. Login title `Авторизація`; Cart title `Кошик`). Note: Wishlist while logged out redirects to Login (route `account/login`) — assert that documented behaviour, not a wishlist page.
- After `page.go_back()`, `page.url` is the base URL again (the home page is restored).
#### Implementation Notes
Drive the four links from a small in-test mapping of `link_locator → (expected_route, expected_title)`, or parametrize over them. Read `href` with `locator.get_attribute("href")`. Keep the "correct destination" expectations derived where possible from the link's own `href`; assert page identity via `page.title()` (native, in the test). Reuse the existing `HomePage` link locators; do not add getter methods for title/url.
#### Done When
- The test verifies non-empty, non-placeholder `href` for all four links.
- The test verifies correct destination route and page identity for each link, including the Wishlist→Login redirect.
- The test verifies browser Back restores the home page for each hop.
- The test passes.

### Task 3 — Multi-level menu journey and breadcrumb walk-back
#### Scenario
A shopper drills from a top-level category into a nested subcategory, then uses the breadcrumb to climb back to the parent. This exercises the menu dropdown, the multi-level breadcrumb, and history restoration in one end-to-end journey.
#### Preconditions
The home page is open; a top-level category with at least one subcategory is known (e.g. Desktops → its `Mac`/`PC` subcategory — confirm the actual subcategory name and link in DevTools).
#### Steps
1. Open the home page and open a top-level category.
2. From within that category (or its menu dropdown), open a nested subcategory.
3. Read the subcategory heading and full breadcrumb.
4. Click the **parent** entry in the breadcrumb to navigate back up.
5. Read the restored parent page's heading and breadcrumb.
#### Expected Results (automate as plain asserts)
- On the subcategory page the breadcrumb shows the full hierarchy in order: `Головна` → parent category name → subcategory name (assert each expected fragment is present, and that the parent appears before the subcategory in the breadcrumb text).
- The subcategory `h1` matches the chosen subcategory name.
- After clicking the parent breadcrumb link, the parent category is restored: its `h1` equals the parent category name and `page.url` contains the parent route.
- The restored parent breadcrumb no longer contains the subcategory name (you climbed a level, you did not stay).
#### Implementation Notes
Extend `CategoryPage` with an action to open a subcategory link by visible text, and a helper to click a breadcrumb entry by its link text (e.g. a `breadcrumb.get_by_role("link", name=...)` locator). Subcategory routes may use `index.php?route=product/category&path=...` — derive the expected fragment from the link's `href` rather than guessing. Assertions on ordering can compare `.index()` positions within the breadcrumb `inner_text()`. No `expect()`; all checks are plain `assert` in the test.
#### Done When
- The test performs the full journey: home → category → subcategory → back to parent via breadcrumb.
- Breadcrumb hierarchy, subcategory heading, and restored-parent identity are all asserted.
- The test confirms the subcategory name is gone from the parent breadcrumb after walk-back.
- The test passes.

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
│   ├── home_page.py        # extended: open_category() + header link locators
│   ├── product_page.py     # from Lesson 01
│   ├── cart_page.py        # from Lesson 01
│   └── category_page.py    # new this lesson: heading, breadcrumb, products, subcategory action
└── tests/
    ├── test_smoke.py
    ├── test_home_page.py   # from Lesson 01
    └── test_navigation.py  # new this lesson
```

## Git Workflow Reminder
Work on branch `lesson-02`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Prove a navigation reached the right destination by cross-checking route, heading, and breadcrumb — not just that the URL changed.
- Derive expected routes from a link's own `href` instead of hardcoding volatile URLs.
- Parametrize a single navigation test across several categories.
- Walk a multi-level hierarchy and use breadcrumb links to climb back, confirming the restored parent page.
- Keep Page Objects thin (locators + actions) with every `assert` living in the test.
