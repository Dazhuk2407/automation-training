"""Вправа 2: знайди і виправ баг.

Один із тестів падає через `# BUG:`. Знайди рядок, виправ його,
щоб усі 4 тести проходили. НЕ змінюй тести.
"""
import logging

logger = logging.getLogger("ex2")


def log_result(log, success):
    if success:
        log.info("test passed")
    else:
        # BUG: падіння тесту має логуватися на рівні ERROR, а не INFO
        log.info("test failed")
    return success

def log_flaky(log, message):
    log.warning("flaky: %s", message)
    return message

def test_pass_logs_info(caplog):
    with caplog.at_level(logging.INFO, logger="ex2"):
        log_result(logger, True)
    assert "test passed" in caplog.text

def test_fail_logs_error(caplog):
    with caplog.at_level(logging.ERROR, logger="ex2"):
        log_result(logger, False)
    assert "test failed" in caplog.text

def test_log_result_returns_value():
    assert log_result(logger, True) is True

def test_flaky_warns(caplog):
    with caplog.at_level(logging.WARNING, logger="ex2"):
        log_flaky(logger, "slow response")
    assert "flaky: slow response" in caplog.text
