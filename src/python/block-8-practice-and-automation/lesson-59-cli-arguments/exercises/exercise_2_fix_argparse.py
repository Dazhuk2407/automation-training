"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_argparse.py -v

Один з add_argument має помилку (# BUG:). Знайди її та виправ,
щоб усі 4 тести проходили.
"""
import argparse


def build_parser():
    parser = argparse.ArgumentParser(description="QA runner")
    parser.add_argument("--env", default="dev", choices=["dev", "staging", "prod"])
    # BUG: немає type=int, тому retries залишається рядком
    parser.add_argument("--retries", default=0)
    parser.add_argument("--headless", action="store_true")
    return parser


def test_default_env():
    assert build_parser().parse_args([]).env == "dev"


def test_retries_is_int():
    assert build_parser().parse_args(["--retries", "3"]).retries == 3


def test_headless_flag():
    assert build_parser().parse_args(["--headless"]).headless is True


def test_headless_default():
    assert build_parser().parse_args([]).headless is False
