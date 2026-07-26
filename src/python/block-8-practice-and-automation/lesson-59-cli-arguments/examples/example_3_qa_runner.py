"""Приклад 3: QA test runner з --suite, --env, --headless.
Запуск: pytest example_3_qa_runner.py -v"""
import argparse


def build_parser():
    parser = argparse.ArgumentParser(description="QA test runner")
    parser.add_argument("--suite", default="smoke",
                        choices=["smoke", "regression", "full"])
    parser.add_argument("--env", default="dev",
                        choices=["dev", "staging", "prod"])
    parser.add_argument("--retries", type=int, default=0)
    parser.add_argument("--headless", action="store_true")
    return parser


def describe(args):
    return f"{args.suite} on {args.env} (retries={args.retries}, headless={args.headless})"


def test_runner_defaults():
    args = build_parser().parse_args([])
    assert args.suite == "smoke"
    assert args.env == "dev"
    assert args.retries == 0
    assert args.headless is False


def test_runner_full_config():
    args = build_parser().parse_args(
        ["--suite", "regression", "--env", "staging", "--retries", "2", "--headless"]
    )
    assert args.suite == "regression"
    assert args.env == "staging"
    assert args.retries == 2
    assert args.headless is True


def test_describe():
    args = build_parser().parse_args(["--suite", "full", "--env", "prod"])
    assert describe(args) == "full on prod (retries=0, headless=False)"


def test_bad_suite_exits():
    import pytest
    with pytest.raises(SystemExit):
        build_parser().parse_args(["--suite", "unit"])
