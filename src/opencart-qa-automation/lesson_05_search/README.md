# Lesson 05: Search

## Goal
Automate the OpenCart search feature as a real user experiences it: submit a query from the header, land on the results page, and judge whether the results actually answer the query. You will verify that returned cards are *relevant* (not merely present), handle negative and boundary inputs including the exact no-results message, and drive a data-driven **search matrix** where every input carries its own expected outcome.

## Theory
- The header search is a text input (`input[name='search']`) plus a search button. Typing a term and submitting navigates to the results route `index.php?route=product/search&search=<term>`, so both the route and the submitted term are observable in the URL.
- A **positive** search returns product cards (`.product-thumb`). Relevance matters: a result set that "has cards" is not automatically correct — the cards should relate to what was typed.
- A **negative** search (a term nothing matches) returns **zero** cards and shows the exact message `Немає продуктів які б відповідали критеріям пошуку.` ("There are no products that match the search criteria.").
- **Boundary inputs** — empty and whitespace-only queries — are their own category: submit them and observe what state the store actually renders, rather than assuming.
- **Where code lives:** the search *action* belongs on `HomePage` (the box is in every page header); the *result-page* reading (cards, no-results message) belongs in a `SearchResultsPage`. Assertions live only in tests.
- **Data-driven testing:** when the same steps run for many inputs, don't copy the test — `@pytest.mark.parametrize` runs the body once per row and reports each as its own named case.
- **`pytest -k` (dev aid, not homework):** `-k` filters tests by a substring of their *name* so you can iterate on a subset. `pytest -k search` runs every test whose name contains `search`; `pytest -k "relevance or matrix"` runs either. (`-k` selects by name; `-m`, later, selects by marker.)

## New Concepts
- `locator.fill(text)` to enter a query (clears + types in one step); submitting via the search button.
- Reading the submitted query back from `page.url` to prove *what* was searched.
- **Relevance checking:** looping over `.product-thumb` cards and asserting their text relates to the term, instead of only counting them.
- Asserting a results state vs a **no-results** state, using the exact message text.
- `@pytest.mark.parametrize` with a **row per case** carrying input + expected state + expected text.

## Practical Explanation

### 1. The `search(term)` action on `HomePage`
```python
# pages/home_page.py
from pages.base_page import BasePage


class HomePage(BasePage):
    PATH = ""

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("input[name='search']")
        self.search_button = page.locator("div#search button")

    def open(self):
        super().open(self.PATH)

    def search(self, term):
        self.search_input.fill(term)   # clears + types in one step
        self.search_button.click()     # submit -> results page
```

### 2. A `SearchResultsPage` for reading results (no assertions inside)
```python
# pages/search_results_page.py
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_cards = page.locator(".product-thumb")
        self.no_results_message = page.get_by_text(
            "Немає продуктів які б відповідали критеріям пошуку."
        )

    def card_names(self):
        """Return the visible product name of every result card."""
        names = []
        for i in range(self.product_cards.count()):
            names.append(self.product_cards.nth(i).locator("h4 a").inner_text())
        return names
```

### 3. Relevance beats a bare count (plain asserts, in the test)
Counting cards only proves the page rendered *something*. A relevance check proves the results answer the query. Assertions are ordinary `assert` statements — no `expect()`.

```python
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_search_results_are_relevant(page):
    home_page = HomePage(page)
    home_page.open()
    home_page.search("iphone")

    assert "route=product/search" in page.url
    assert "search=iphone" in page.url.lower()

    results = SearchResultsPage(page)
    names = results.card_names()
    assert names, "expected at least one result card"
    assert all("iphone" in name.lower() for name in names)
```

### 4. A parametrized matrix — one row, three expectations
Each row carries the **input**, the **expected state** (results vs no-results), and the **expected text** (a substring that must appear in a card, or the no-results message).

```python
import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

NO_RESULTS = "Немає продуктів які б відповідали критеріям пошуку."

@pytest.mark.parametrize("term, has_results, expected_text", [
    ("iPhone",   True,  "iphone"),      # exact product name
    ("phone",    True,  "phone"),       # partial term
    ("IPHONE",   True,  "iphone"),      # different case
    ("qwertyzzz", False, NO_RESULTS),   # no-result term
])
def test_search_matrix(page, term, has_results, expected_text):
    home_page = HomePage(page)
    home_page.open()
    home_page.search(term)

    results = SearchResultsPage(page)
    if has_results:
        names = [n.lower() for n in results.card_names()]
        assert names, f"expected results for {term!r}"
        assert any(expected_text in n for n in names)
    else:
        assert results.product_cards.count() == 0
        assert results.no_results_message.is_visible()
        assert expected_text in results.no_results_message.inner_text()
```

Run `pytest -v` and each row prints as its own case (`test_search_matrix[iPhone-True-iphone]`, …). While iterating, `pytest -k matrix` runs just this test.

> Tip: the selectors above are illustrative. Confirm the real ones in DevTools (right-click → Inspect): the **search input**, the **search button**, the **product cards**, the **card name element**, and the **no-results message**. Verifying locators is a core QA skill — that is why they live inside Page Objects where they are easy to fix.

## Homework
Do all three tasks on a branch named `lesson-05`. Assertions go **only** in test files, as plain `assert` statements — no `expect()`. **Do not assert only `count() > 0`**: prove the results are relevant. Do not hardcode volatile prices, exact counts, or product positions.

### Task 1 — Search-result relevance
#### Scenario
A customer searches for a product by name and expects the results page to show that product, not an unrelated grab-bag. This verifies that the search is wired correctly and that every returned card actually relates to the submitted term.
#### Preconditions
Store home page is reachable; `HomePage.search(term)` and a `SearchResultsPage` that can read each card's name are available (add them this lesson).
#### Steps
1. Open the store home page.
2. Search a complete product name (e.g. `"iPhone"`).
3. Read the URL to confirm the route and the submitted query.
4. Read the name of every result card.
5. Open one result and read the product page identity (H1 / title).
#### Expected Results (automate as plain asserts)
- `route=product/search` is present in `page.url` and the submitted term appears in the URL query (`search=` value).
- At least one result card is returned (the names list is non-empty).
- **Every** returned card's name is relevant to the term (case-insensitive substring / term match) — not just `count() > 0`.
- After opening one result, its product page identity (H1 or title) matches the card you selected.
#### Implementation Notes
Add `search(term)` to `HomePage` (locators in `__init__`). Create `pages/search_results_page.py` with `SearchResultsPage(BasePage)` exposing the card collection, the no-results message, and a helper that returns card names (e.g. `card_names()`). Reuse the existing `page` fixture and `BasePage.open()`. Keep the relevance loop and all asserts in the test.
#### Done When
- `HomePage.search(term)` and `SearchResultsPage` exist, locators in `__init__`, no assertions inside them.
- The test asserts route + submitted query + non-empty results + per-card relevance + opened-product consistency.
- DevTools: search input, search button, product card, and card-name element confirmed.

### Task 2 — Negative and boundary search
#### Scenario
Search must fail gracefully. A nonsense term, an empty query, and a whitespace-only query are all inputs a real user can submit; each should land in a defined state with no stale results from a previous search bleeding through.
#### Preconditions
`HomePage.search(term)` and `SearchResultsPage` from Task 1 exist.
#### Steps
1. Open the store and search a nonsense term (e.g. `"qwertyzzz"`).
2. Observe the results state and the message.
3. In fresh page states, submit an **empty** query and a **whitespace-only** query (e.g. `"   "`).
4. Record what state each actually renders (results, no-results message, or the search landing) — verify in DevTools first.
#### Expected Results (automate as plain asserts)
- For the nonsense term: product-card count is exactly `0`, **and** the exact message `Немає продуктів які б відповідали критеріям пошуку.` is visible and its text matches exactly.
- For the boundary inputs (empty / whitespace): assert the actual defined state you confirmed — either the no-results message is shown, or zero relevant cards are present. Do not assume; assert what the store really does.
- No unrelated stale results survive: after a no-results search, no relevant card from an earlier positive search remains (card count is `0`).
#### Implementation Notes
Reuse `SearchResultsPage.no_results_message` and `product_cards`. Assert the message with `is_visible()` plus an exact-text check (`== ` or exact `in`), not a loose substring. Give each scenario its own test (or clearly named cases) so a failure points to the exact input class. Confirm the empty/whitespace behavior in DevTools before encoding the expectation.
#### Done When
- Nonsense term asserts `count() == 0` and the exact no-results message.
- Empty and whitespace inputs each assert their confirmed real state.
- A test proves no stale results persist after a no-results search.
- DevTools: no-results message and product cards confirmed.

### Task 3 — Parametrized search matrix
#### Scenario
Instead of one test per input, drive the search with a single data-driven matrix where each row is a QA test case: an input, the expected result state, and the expected text (a card substring for hits, or the no-results message for misses). This is the maintainable way real suites cover many inputs.
#### Preconditions
Tasks 1–2 complete; `HomePage.search` and `SearchResultsPage` (with `card_names()`) available.
#### Steps
1. Define a parametrize table with at least four rows: exact product name, partial name, different letter-case of a valid term, and a no-result term.
2. Give each row an `expected_state` (has-results vs no-results) and an `expected_text`.
3. In the test body, search the row's term.
4. Branch on `expected_state` and assert the matching expectation for that row.
#### Expected Results (automate as plain asserts)
- Each hit row: results are non-empty **and** at least one card name contains that row's `expected_text` (relevance — not merely `count() > 0`).
- The no-result row: card count is `0` **and** the no-results message text equals that row's `expected_text`.
- `pytest -v` shows every row as its own named case.
#### Implementation Notes
Use `@pytest.mark.parametrize("term, expected_state, expected_text", [...])` (or an equivalent id-per-row layout). Store the no-results constant once and reference it in both the row data and the assertion. Reuse the `page` fixture and the Page Objects from Tasks 1–2 — no duplicated setup. Keep the branching (has-results vs no-results) inside the test.
#### Done When
- One parametrized test covers exact-name, partial, different-case, and no-result rows.
- Hit rows assert relevance via card text; the miss row asserts `count() == 0` + exact message.
- No row asserts only `count() > 0`.
- `pytest -v` lists each row as a distinct case; `pytest -k` can select the search tests.

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
│   ├── home_page.py            # gains search(term) this lesson
│   ├── category_page.py
│   ├── product_page.py
│   └── search_results_page.py  # NEW this lesson
└── tests/
    ├── test_smoke.py
    ├── test_navigation.py
    ├── test_locators.py
    ├── test_assertions.py
    └── test_search.py          # NEW this lesson
```

## Git Workflow Reminder
Work on branch `lesson-05`, commit, push, open a Pull Request into `main`, and merge only after approval — see Lesson 00 for the full workflow.

## After completing this lesson you should be able to...
- Drive a search from a `HomePage` action and read results through a dedicated `SearchResultsPage`, with assertions kept in tests as plain `assert`s.
- Judge result **relevance** by inspecting card content, not by counting cards alone.
- Verify negative and boundary searches, including the exact no-results message and the absence of stale results.
- Build a data-driven **search matrix** with `@pytest.mark.parametrize` where each row carries its input, expected state, and expected text.
- Use `pytest -k` to run a subset of tests by name while developing.
