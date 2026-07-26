"""Вправа 2: Виправити баг у роботі з CSV. Запуск: pytest exercise_2_fix_csv.py -v

Тести нижче падають — рівно один. Знайдіть рядок з коментарем `# BUG:`
і виправте його, щоб усі 4 тести проходили.
"""
import csv


def save_users(path, users, fieldnames):
    """Зберегти список словників у CSV із заголовком."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)


def read_users(path):
    """Прочитати CSV як список словників."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def get_names(path):
    """Повернути список імен користувачів із CSV."""
    # BUG: читаємо не ту колонку — беремо row["age"] замість row["name"],
    #      тож повертаються вік, а не імена.
    #      Треба: return [row["name"] for row in read_users(path)]
    return [row["age"] for row in read_users(path)]


def test_header_written(tmp_path):
    p = tmp_path / "users.csv"
    save_users(p, [{"name": "Alice", "age": "30"}], ["name", "age"])
    assert p.read_text(encoding="utf-8").splitlines()[0] == "name,age"


def test_roundtrip_count(tmp_path):
    p = tmp_path / "users.csv"
    save_users(p, [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}], ["name", "age"])
    assert len(read_users(p)) == 2


def test_read_age(tmp_path):
    p = tmp_path / "users.csv"
    save_users(p, [{"name": "Alice", "age": "30"}], ["name", "age"])
    assert read_users(p)[0]["age"] == "30"


def test_get_names(tmp_path):
    p = tmp_path / "users.csv"
    save_users(p, [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}], ["name", "age"])
    assert get_names(p) == ["Alice", "Bob"]
