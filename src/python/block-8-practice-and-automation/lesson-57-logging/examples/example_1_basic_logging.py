"""Приклад 1: logging проти print. Запуск: pytest example_1_basic_logging.py -v"""
import logging


def level_value(name):
    return logging.getLevelName(name)

def level_name(value):
    return logging.getLevelName(value)

def is_enabled(msg_level, min_level):
    return msg_level >= min_level

def test_level_value():
    assert level_value("INFO") == 20
    assert level_value("ERROR") == 40

def test_level_name():
    assert level_name(30) == "WARNING"
    assert level_name(10) == "DEBUG"

def test_is_enabled():
    assert is_enabled(logging.ERROR, logging.WARNING) is True
    assert is_enabled(logging.DEBUG, logging.WARNING) is False

def test_info_logged(caplog):
    logger = logging.getLogger("example1")
    with caplog.at_level(logging.INFO, logger="example1"):
        logger.info("User created")
    assert "User created" in caplog.text
