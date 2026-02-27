# Exercises - Lesson 1: Install Pytest

## Exercise 1: Install pytest (EASY)

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install pytest
pip install pytest

# Verify installation
pytest --version
```

**Expected output:**
```
pytest 7.x.x
```

---

## Exercise 2: Create requirements.txt (EASY)

Create `requirements.txt`:

```txt
pytest==7.4.3
```

Install from requirements:

```bash
pip install -r requirements.txt
```

---

## Exercise 3: Check pytest help (MEDIUM)

```bash
# View pytest help
pytest --help

# Find answers:
# 1. How to run only failed tests?
# 2. How to run tests in parallel?
# 3. How to show local variables in tracebacks?
```

---

## Exercise 4: Verify pytest plugins (MEDIUM)

```bash
# Check installed plugins
pytest --version --verbose

# Install additional plugin
pip install pytest-cov

# Verify it's installed
pytest --version --verbose
```

---

**Ready for Lesson 2?** 🚀

