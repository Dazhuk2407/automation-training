"""Модуль strings у пакеті mypackage."""


def shout(s):
    return s.upper() + "!"


def is_empty(s):
    return len(s.strip()) == 0
