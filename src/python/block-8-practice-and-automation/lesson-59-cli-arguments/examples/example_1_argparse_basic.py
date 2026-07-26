"""Приклад 1: базовий argparse та позиційні аргументи.
Запуск: pytest example_1_argparse_basic.py -v"""
import argparse


def build_greet_parser():
    parser = argparse.ArgumentParser(description="Привітати користувача")
    parser.add_argument("name")
    return parser


def build_copy_parser():
    parser = argparse.ArgumentParser(description="Скопіювати файл")
    parser.add_argument("source")
    parser.add_argument("dest")
    return parser


def test_single_positional():
    args = build_greet_parser().parse_args(["Alice"])
    assert args.name == "Alice"


def test_two_positionals():
    args = build_copy_parser().parse_args(["a.txt", "b.txt"])
    assert args.source == "a.txt"
    assert args.dest == "b.txt"


def test_missing_positional_exits():
    import pytest
    with pytest.raises(SystemExit):
        build_greet_parser().parse_args([])


def test_positional_is_string():
    args = build_greet_parser().parse_args(["42"])
    assert args.name == "42"
    assert isinstance(args.name, str)
