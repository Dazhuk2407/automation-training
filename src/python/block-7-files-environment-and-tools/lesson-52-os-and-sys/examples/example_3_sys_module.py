"""Приклад 3: модуль sys. Запуск: pytest example_3_sys_module.py -v"""
import sys


def script_name(argv):
    # argv[0] — це імʼя скрипта, а не перший аргумент
    return argv[0]


def script_args(argv):
    # Реальні аргументи починаються з індексу 1
    return argv[1:]


def python_major():
    return sys.version_info.major


def is_windows():
    return sys.platform.startswith("win")


def test_script_name():
    assert script_name(["run.py", "smoke", "fast"]) == "run.py"


def test_script_args():
    assert script_args(["run.py", "smoke", "fast"]) == ["smoke", "fast"]
    assert script_args(["run.py"]) == []


def test_python_major():
    assert python_major() == 3


def test_sys_path_is_list():
    assert isinstance(sys.path, list)


def test_is_windows_matches_platform():
    assert is_windows() == sys.platform.startswith("win")
