"""Приклад 3: Діф двох freeze-наборів. Запуск: pytest example_3_freeze_diff.py -v

Порівнюємо два 'freeze' як dict {name: version}. Реальний pip не викликається.
"""


def freeze_to_dict(lines):
    """['pytest==7.4.0', 'requests==2.31.0'] -> {'pytest': '7.4.0', 'requests': '2.31.0'}."""
    result = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, version = line.split("==", 1)
        result[name.strip()] = version.strip()
    return result


def diff_freezes(old, new):
    """Порівняти два набори {name: version}.

    Повертає dict з ключами 'added', 'removed', 'changed'.
    """
    added = {k: new[k] for k in new if k not in old}
    removed = {k: old[k] for k in old if k not in new}
    changed = {
        k: (old[k], new[k]) for k in old if k in new and old[k] != new[k]
    }
    return {"added": added, "removed": removed, "changed": changed}


def test_freeze_to_dict():
    lines = ["pytest==7.4.0", "requests==2.31.0"]
    assert freeze_to_dict(lines) == {"pytest": "7.4.0", "requests": "2.31.0"}


def test_diff_added():
    old = {"pytest": "7.4.0"}
    new = {"pytest": "7.4.0", "requests": "2.31.0"}
    assert diff_freezes(old, new)["added"] == {"requests": "2.31.0"}


def test_diff_removed():
    old = {"pytest": "7.4.0", "flask": "2.0.0"}
    new = {"pytest": "7.4.0"}
    assert diff_freezes(old, new)["removed"] == {"flask": "2.0.0"}


def test_diff_changed():
    old = {"pytest": "7.4.0"}
    new = {"pytest": "7.4.1"}
    assert diff_freezes(old, new)["changed"] == {"pytest": ("7.4.0", "7.4.1")}


def test_diff_no_changes():
    same = {"pytest": "7.4.0"}
    result = diff_freezes(same, dict(same))
    assert result == {"added": {}, "removed": {}, "changed": {}}
