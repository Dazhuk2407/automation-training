"""Приклад 2: опції — default, type, choices, required, store_true.
Запуск: pytest example_2_options.py -v"""
import argparse


def build_parser():
    parser = argparse.ArgumentParser(description="Конфіг запуску")
    parser.add_argument("--env", default="dev", choices=["dev", "staging", "prod"])
    parser.add_argument("--retries", type=int, default=0)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def build_required_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", required=True)
    return parser


def test_defaults():
    args = build_parser().parse_args([])
    assert args.env == "dev"
    assert args.retries == 0
    assert args.verbose is False
    assert args.dry_run is False


def test_parse_all():
    args = build_parser().parse_args(
        ["--env", "prod", "--retries", "3", "--verbose", "--dry-run"]
    )
    assert args.env == "prod"
    assert args.retries == 3
    assert args.verbose is True
    assert args.dry_run is True


def test_type_int():
    args = build_parser().parse_args(["--retries", "5"])
    assert args.retries == 5
    assert isinstance(args.retries, int)


def test_invalid_choice_exits():
    import pytest
    with pytest.raises(SystemExit):
        build_parser().parse_args(["--env", "qa"])


def test_required_missing_exits():
    import pytest
    with pytest.raises(SystemExit):
        build_required_parser().parse_args([])


def test_required_provided():
    args = build_required_parser().parse_args(["--token", "abc123"])
    assert args.token == "abc123"


def test_dash_becomes_underscore():
    args = build_parser().parse_args(["--dry-run"])
    assert args.dry_run is True
