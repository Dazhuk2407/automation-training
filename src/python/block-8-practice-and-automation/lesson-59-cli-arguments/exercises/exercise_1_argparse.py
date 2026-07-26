"""Вправа 1: argparse. Запуск: pytest exercise_1_argparse.py -v"""
import argparse


def build_parser():
    # TODO: створити ArgumentParser
    # TODO: add_argument("--env", default="dev", choices=["dev", "prod"])
    # TODO: add_argument("--retries", type=int, default=0)
    # TODO: add_argument("--verbose", action="store_true")
    # TODO: return parser
    pass


def test_default_env():
    # TODO: assert build_parser().parse_args([]).env == "dev"
    pass


def test_default_retries():
    # TODO: assert build_parser().parse_args([]).retries == 0
    pass


def test_default_verbose():
    # TODO: assert build_parser().parse_args([]).verbose is False
    pass


def test_parse_retries_int():
    # TODO: assert build_parser().parse_args(["--retries", "3"]).retries == 3
    pass


def test_parse_verbose_flag():
    # TODO: assert build_parser().parse_args(["--verbose"]).verbose is True
    pass
