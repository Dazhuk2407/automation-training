# OpenCart QA Automation — Playwright + Python (Functional Coverage → Portfolio)

A hands-on, project-based course that builds a **portfolio-ready UI automation framework** with **~30 real, functional automated tests**. It assumes you already know **basic Python, pytest, fixtures, assertions, and basic Page Object ideas** — so from Lesson 01 the homework is real QA-Automation work, not beginner warm-ups. You practise on a real, public store — **[demo.opencart.ua](https://demo.opencart.ua)** — used purely as a training playground.

- **Practice site:** https://demo.opencart.ua (real, stable, automatable)
- **Stack:** Python · pytest · Playwright · pytest-playwright · Page Object Model
- **Workflow you practise:** Git + GitHub — branch per lesson → Pull Request → review → merge
- **You finish with:** a clean framework, ~30 UI tests, and a GitHub repo you can show employers.

---

## How the course works

- **11 lessons, 00 → 10.** **Lesson 00 does all the setup** (environment, framework, `config.py`, `BasePage`, `conftest.py`, `pytest.ini`, repo, Git workflow). **From Lesson 01 every lesson is real functional coverage** of OpenCart — no setup is repeated.
- **Exactly 3 functional homework tasks per lesson**, each written as a mini QA backlog item (Scenario / Preconditions / Steps / Expected Results / Implementation Notes / Done When) and growing in difficulty: Task 1 positive journey → Task 2 data-variation / negative → Task 3 state-changing / end-to-end.
- **You build one framework and grow it** lesson by lesson — you never rebuild it. Locators live **inside Page Objects**; Page Objects hold locators/navigation/actions only.
- **Assertions are plain Python `assert` in test files** (run by pytest). This course does **not** use Playwright `expect()`. Page Objects contain no assertions.
- **Real Git workflow:** push only to **your own** GitHub repo, work each lesson on its own branch, and merge into `main` **only after a Pull Request is reviewed and approved** — never commit directly to `main`.

## Architecture you build

```
pages/          # Page Objects (one per page) + base_page.py — locators live here, inside __init__
tests/          # test files — scenarios and assertions
utils/          # reusable test-data helpers — added in Lesson 06 (unique_email, generate_user_data)
config.py       # BASE_URL and settings
conftest.py     # ALL shared pytest fixtures live here (e.g. logged_in_page) + shared config
pytest.ini      # runner config + markers (smoke/regression)
requirements.txt · README.md · .gitignore
```

> Convention: **all shared fixtures live in `conftest.py`** — there is no separate `fixtures/` directory. BasePage exposes a single navigation method, **`open(path="")`**, used by every Page Object.

## Roadmap

| # | Lesson | You learn / build |
|---|--------|-------------------|
| 00 | Environment, Framework Bootstrap & Git | **All setup**: tools, framework (`config.py`/`BasePage`/`conftest.py`/`pytest.ini`), repo + branch → PR → merge |
| 01 | Home Page | featured-card consistency, dynamic product navigation, home-to-cart journey |
| 02 | Navigation | parametrized category navigation, header nav map, multi-level breadcrumb journey |
| 03 | Locators | validate every card, compare two scoped cards, find a product by its content |
| 04 | Assertions | assertion design with plain pytest `assert`; structural, cross-page & derived checks |
| 05 | Search | result relevance, negative/boundary search, parametrized search matrix |
| 06 | Registration | full registration, required-field validation matrix, duplicate & data-integrity |
| 07 | Login | positive session, invalid-credential matrix, session state transitions |
| 08 | Shopping Cart & State Fixtures | product-to-cart consistency, quantity & calculated totals, multi-item transitions |
| 09 | Wishlist & Account | authorization gate, wishlist state transitions, wishlist-to-cart journey |
| 10 | Regression & Framework Quality | risk-based markers, critical E2E regression, stability audit, portfolio README |

## How to work a lesson

1. Read the lesson `README.md` (Goal → Theory → New Concepts → Practical Explanation).
2. Do the **3 homework tasks** in order.
3. Run your tests; check each task's **Done when** list.
4. Commit on the lesson branch, open a Pull Request, get it approved, merge.

> The code examples show you the *pattern*. The homework is where **you** write the automation — that is the skill this course trains.
