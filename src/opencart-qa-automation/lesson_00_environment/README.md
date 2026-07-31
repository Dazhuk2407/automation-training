# Lesson 00: Environment, Framework Bootstrap & Git Workflow

## Goal
This is the one and only setup lesson. By the end you own a complete, working test-automation framework and the professional workflow to ship it. You install the toolchain (Python, a code editor, Git, Playwright), create your own GitHub repository, and bootstrap the framework skeleton every later lesson extends: `config.py`, `pages/base_page.py`, `conftest.py`, `pytest.ini`, `.gitignore`, and pinned `requirements.txt`. You finish with a tiny smoke test — written as a plain `assert` — that opens https://demo.opencart.ua and proves the whole stack runs. From Lesson 01 onward there is NO more setup: you just write tests.

## Theory
- **Python** runs your tests; a **code editor — VS Code or PyCharm — is your choice**, pick whichever you prefer.
- **A virtual environment (`venv`)** isolates this project's packages; **`requirements.txt`** pins them so the environment is reproducible with one command.
- **Playwright** drives the browser. Installing it is two steps: the Python package (`pip install`) and the browser binaries (`playwright install`).
- **`pytest`** is the test runner; **`pytest-playwright`** injects a ready `page` object into every test.
- **Git** is local version control; **GitHub** hosts the repo and is where Pull Requests live.
- **The golden rule:** you NEVER commit directly to `main`. Every change lands on `main` only through a reviewed, approved, merged Pull Request.

## New Concepts
- Installing and verifying the toolchain: Python, VS Code / PyCharm, Git, Playwright (package + browsers).
- Creating a GitHub account and your own course repository, then the flow `clone → branch → commit → push → Pull Request → review → merge`; branch-per-lesson naming (`lesson-00`, `lesson-01`, …).
- The framework skeleton: `pages/`, `tests/`, `config.py`, `conftest.py`, `pytest.ini`, `.gitignore`, `requirements.txt` (the `utils/` package arrives later, in Lesson 06).
- **Architecture conventions used for the whole course** (see below): locators live inside Page Objects, one Page Object style (`PATH` constant + no-arg `open()`), and **assertions are plain `assert` statements in test files — never Playwright `expect()`**.

### Architecture conventions (the rules for every lesson)
- **Page Objects hold locators, navigation and actions — never assertions.** Every selector is defined in a Page Object's `__init__`. There is no `locators/` folder and no locator classes.
- **One Page Object style:** each page inherits `BasePage`, defines a `PATH` constant, and exposes a **no-arg `open()`** that opens that path.
- **`BasePage.open(path="")`** joins `BASE_URL` and the path with an rstrip/lstrip trim so they always combine cleanly.
- **Config lives in `config.py`** (`BASE_URL`) — nothing is hardcoded in tests.
- **Fixtures live only in `conftest.py`** — there is no `fixtures/` folder.
- **Assertions are plain `assert` in test files.** We do NOT use `expect(...)` and never `from playwright.sync_api import expect`. A test asks a business question with ordinary Python asserts, e.g. `assert "OpenCart" in page.title()`, `assert locator.is_visible()`, `assert locator.count() > 0`.

## Practical Explanation

### 1. Verify your tools from the terminal
If a command prints a version, it is installed and on your `PATH`:
```bash
python --version      # e.g. Python 3.12.4  (some systems: python3 --version)
git --version         # e.g. git version 2.45.2
code --version        # VS Code version (PyCharm users: launch the IDE instead)
```

### 2. One-time Git identity
```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

### 3. Virtual environment, dependencies, browsers
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install                # downloads the browser binaries
```
`requirements.txt`:
```text
pytest
playwright
pytest-playwright
```

### 4. The framework skeleton (create these once)
`config.py` — the single source of truth for the base URL:
```python
# config.py
BASE_URL = "https://demo.opencart.ua"
```

`pages/base_page.py` — the parent of every Page Object. It holds the `page` and knows how to open a path relative to `BASE_URL`:
```python
# pages/base_page.py
from config import BASE_URL


class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, path=""):
        url = f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}"
        self.page.goto(url)
```

`pages/home_page.py` — a first Page Object showing the standard style (`PATH` + no-arg `open()`):
```python
# pages/home_page.py
from pages.base_page import BasePage


class HomePage(BasePage):
    PATH = ""                      # home is the site root

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("input[name='search']")

    def open(self):
        super().open(self.PATH)
```

`pytest.ini` — keeps `pytest-playwright` options in one place:
```ini
[pytest]
addopts = --headed --browser chromium
```

`.gitignore` — never commit the venv, caches, or Playwright artifacts:
```text
venv/
__pycache__/
.pytest_cache/
test-results/
*.pyc
```

`conftest.py` — fixtures live here. A small `home_page` fixture keeps tests tidy; richer fixtures (`logged_in_page`, `cart_with_product`) are added in later lessons:
```python
# conftest.py
import pytest

from pages.home_page import HomePage


@pytest.fixture
def home_page(page):
    home = HomePage(page)
    home.open()
    return home
```

### 5. The smoke test — proof the stack works (plain `assert`, no `expect`)
```python
# tests/test_smoke.py
from pages.home_page import HomePage


def test_home_page_loads(page):
    home = HomePage(page)
    home.open()
    assert "OpenCart" in page.title()          # home title is "Демо магазин OpenCart"
```
Run it:
```bash
pytest tests/test_smoke.py
```

### 6. The core Git flow (repeat every lesson)
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

git checkout -b lesson-00          # create + switch to the lesson branch
# ... make your changes ...

git add .
git commit -m "Lesson 00: framework bootstrap"
git push -u origin lesson-00       # publish the branch
```
Then open a Pull Request (Base `main` ← Compare `lesson-00`), self-review the diff, approve, and **Merge**. After merging, refresh local `main` for the next lesson:
```bash
git checkout main
git pull origin main
```

## Homework

### Task 1 — Install the toolchain and ship YOUR repo through a Pull Request
#### Scenario
A professional starts from a clean machine: working tools plus a repository whose `main` branch is protected by a review workflow. You set both up and prove nothing reaches `main` except through a PR.
#### Preconditions
A machine with internet access and a GitHub account (create one if needed).
#### Steps
1. Install Python, a code editor (VS Code **or** PyCharm — your choice), and Git.
2. Set your Git identity (`user.name`, `user.email`).
3. Create a brand-new GitHub repository for the course (e.g. `opencart-qa-automation`) and clone it locally.
4. Create a `lesson-00` branch, add a short `README.md` describing the repo, commit and push.
5. Open a Pull Request from `lesson-00` into `main`, self-review, approve, and merge.
#### Expected Results
- `python --version` (or `python3 --version`), `git --version`, and `code --version` each print a version — or PyCharm launches and opens a project.
- The repo exists in YOUR account, is cloned locally, and its history shows the README arriving via a merged PR — not a direct commit to `main`.
#### Implementation Notes
Use `git config --global` for identity. GitHub prints a PR link right after `git push`. In this course you are your own reviewer.
#### Done When
- All three tools report a version (or the IDE opens).
- A merged PR (`lesson-00` → `main`) is visible in the repo, and `main` received zero direct commits.

### Task 2 — Bootstrap the framework skeleton
#### Scenario
Every later lesson assumes a reproducible environment and a clean, beginner-friendly project layout. You create that foundation once so no lesson ever repeats setup.
#### Preconditions
The cloned repo from Task 1, on a fresh `lesson-00` branch (continue the same branch).
#### Steps
1. Create and activate a virtual environment (`venv`).
2. Add `requirements.txt` (`pytest`, `playwright`, `pytest-playwright`), install it, then run `playwright install`.
3. Create the project structure: `pages/` (with `base_page.py`), `tests/`, and root files `config.py`, `pytest.ini`, `.gitignore`.
4. Put `BASE_URL = "https://demo.opencart.ua"` in `config.py`; implement `BasePage` with `open(path="")` using the rstrip/lstrip URL join.
5. Commit the skeleton (the `.gitignore` must keep `venv/` and caches out of Git).
#### Expected Results
- `pip install -r requirements.txt` and `playwright install` both complete successfully.
- The structure below exists; `config.py` holds the single `BASE_URL`; `BasePage.open()` builds `BASE_URL + path` cleanly.
- `git status` shows `venv/`, `__pycache__/`, and `.pytest_cache/` are ignored, not staged.
#### Implementation Notes
Follow the `config.py`, `base_page.py`, `pytest.ini`, and `.gitignore` snippets in the Practical Explanation. Keep locators out of `BasePage` — it only stores `page` and opens paths.
#### Done When
- The environment installs from `requirements.txt` in one command and browsers are installed.
- `config.py`, `pages/base_page.py`, `pytest.ini`, and `.gitignore` exist and match the conventions.

### Task 3 — Add the first Page Object, a fixture, and a passing smoke test
#### Scenario
The final proof the toolchain runs end to end: a real browser opens the store and a test confirms the home page loaded — verified with a plain `assert`, the only assertion style this course uses.
#### Preconditions
The framework skeleton from Task 2 in place, on the same `lesson-00` branch.
#### Steps
1. Create `pages/home_page.py` as a `HomePage(BasePage)` with a `PATH` constant and a no-arg `open()`.
2. Create `conftest.py` with a `home_page` fixture that opens the home page.
3. Create `tests/test_smoke.py` with a test that opens the home page and asserts the store loaded.
4. Run the smoke test and watch a real browser open the demo store.
5. Commit everything, push, and merge the completed Lesson 00 through its Pull Request.
#### Expected Results
- `pytest tests/test_smoke.py` passes.
- The test uses a plain `assert` (e.g. `assert "OpenCart" in page.title()`) — there is NO `expect(...)` and no `from playwright.sync_api import expect` anywhere.
- `HomePage` exposes `PATH` and a no-arg `open()`; the assertion lives in the test, not in the Page Object.
#### Implementation Notes
Reuse the `home_page.py`, `conftest.py`, and `test_smoke.py` snippets above. Remember the home title is `Демо магазин OpenCart`, so `"OpenCart" in page.title()` is `True`. Keep `HomePage` free of assertions — Page Objects only locate, navigate, and act.
#### Done When
- The smoke test passes against the live site with a real browser.
- The only assertion is a plain `assert`, and the whole Lesson 00 work is merged into `main` via an approved PR.

## Expected Project Structure After This Lesson
```text
opencart-qa-automation/
├── config.py                 # BASE_URL — single source of truth
├── conftest.py               # fixtures (home_page; more added later)
├── pytest.ini                # pytest-playwright options
├── requirements.txt          # pytest, playwright, pytest-playwright
├── .gitignore                # venv/, caches, test-results/
├── README.md
├── pages/
│   ├── base_page.py          # BasePage.open(path="")
│   └── home_page.py          # HomePage: PATH + no-arg open()
└── tests/
    └── test_smoke.py         # plain-assert smoke test
```

## Git Workflow Reminder
Work on a branch named for the lesson (`lesson-00`, `lesson-01`, …), commit and push, open a Pull Request into `main`, self-review and approve, and **merge only after approval — never commit directly to `main`**. This is the workflow every lesson in the course refers back to.

## After completing this lesson you should be able to...
- Verify Python, your editor (VS Code or PyCharm), Git, and Playwright are installed and available.
- Create your own GitHub course repository and run the full flow: branch → commit → push → Pull Request → review → merge, never committing directly to `main`.
- Bootstrap a reproducible framework: `venv`, pinned `requirements.txt`, `config.py`, `BasePage`, `pytest.ini`, `.gitignore`, and `conftest.py` fixtures.
- Write a Page Object in the course style (`PATH` + no-arg `open()`) with locators inside it and no assertions.
- Run a smoke test that opens the live store and verify it with a plain `assert` — no Playwright `expect()`.
