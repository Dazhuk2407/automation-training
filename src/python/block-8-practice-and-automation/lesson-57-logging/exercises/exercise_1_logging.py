"""Вправа 1: logging. Запуск: pytest exercise_1_logging.py -v"""
import logging


def level_name(value):
    # TODO: return logging.getLevelName(value)
    pass

def should_log(msg_level, min_level):
    # TODO: return msg_level >= min_level
    pass

def log_step(logger, step):
    # TODO: logger.info("Step: %s", step); return step
    pass

def test_level_name_info():
    # TODO: assert level_name(20) == "INFO"
    pass

def test_level_name_error():
    # TODO: assert level_name(40) == "ERROR"
    pass

def test_should_log_true():
    # TODO: assert should_log(logging.ERROR, logging.WARNING) is True
    pass

def test_should_log_false():
    # TODO: assert should_log(logging.DEBUG, logging.WARNING) is False
    pass

def test_log_step(caplog):
    # TODO: logger = logging.getLogger("ex1")
    # TODO: with caplog.at_level(logging.INFO, logger="ex1"): log_step(logger, "open")
    # TODO: assert "Step: open" in caplog.text
    pass
