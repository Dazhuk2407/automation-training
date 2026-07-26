"""Приклад 3: іменований логер у функціях. Запуск: pytest example_3_logger.py -v"""
import logging

logger = logging.getLogger(__name__)


def log_step(log, step):
    log.info("Step: %s", step)
    return step

def run_login(log, user, token):
    log.info("login attempt: %s", user)
    if not token:
        log.warning("missing credentials for %s", user)
    success = bool(user and token)
    if not success:
        log.error("login failed for %s", user)
    return success

def test_logger_name():
    assert logger.name == "example_3_logger" or logger.name.endswith("example_3_logger")

def test_log_step(caplog):
    with caplog.at_level(logging.INFO):
        log_step(logger, "open page")
    assert "Step: open page" in caplog.text

def test_run_login_success():
    assert run_login(logger, "alice", "secret") is True

def test_run_login_warns_on_empty(caplog):
    with caplog.at_level(logging.WARNING):
        result = run_login(logger, "bob", "")
    assert result is False
    assert "missing credentials" in caplog.text

def test_run_login_error(caplog):
    with caplog.at_level(logging.ERROR):
        run_login(logger, "", "")
    assert "login failed" in caplog.text
