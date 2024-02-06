#!/usr/bin/env python3
"""
FizzBuzz
========

A slightly over-engineered Python implementation of the classic FizzBuzz game.
"""
import argparse
from collections.abc import Iterable
import dataclasses
from itertools import starmap
from typing import Callable

RuleFunction = Callable[[int], str | None]


class FizzBuzzInt(int):

    def __new__(cls, n: int, rules: Iterable[RuleFunction]):
        return super().__new__(cls, n)

    def __init__(self, _, rules: Iterable[RuleFunction]):
        self.replacements = list(filter(None, map(self._applyRule, rules)))

    def _applyRule(self, rule_function: RuleFunction) -> str | None:
        match rule_function(self):
            case str(r):
                return r
            case None:
                return None
            case _:
                raise TypeError('Rule function returned unknown type.')

    def __str__(self):
        if self.replacements:
            return ''.join(self.replacements)
        return super().__str__()


def make_rule_function(z: int, word: str) -> RuleFunction:
    """
    Create a function that will return the specified ``word`` if ``n``
    divides ``z`` evenly. Otherwise, return an empty string.

    :param z: The divisor.
    :param word: The word to be substituted.
    """
    def sub(n: int) -> str | None:
        return word if n % z == 0 else None

    return sub


def create_rules(
        substitutions: Iterable[tuple[int, str]] | None = None
) -> list[RuleFunction]:
    """
    Create rules.

    :param substitutions: A list of tuples. Each tuple should contain an integer
            for the divisibility test followed by the word that should replace
            the number if it passes the divisibility test. If ``None`` is given,
            classic FizzBuzz rules using 3 and 5 are used.
    :return: A list of rule functions.
    """
    if substitutions is None:
        substitutions = [(3, 'fizz'), (5, 'buzz')]
    return list(starmap(make_rule_function, substitutions))


def fizzbuzz(until: int = 101,
             rules: list[RuleFunction] | None = None) -> list[FizzBuzzInt]:
    """
    Play the FizzBuzz game.

    :param until: The number to count up to (exclusive).
    :param rules: A list of rule functions. If ``None`` is given, classic
            FizzBuzz rules using 3 and 5 are used. Words are stacked
            such that the number 15 will yield "fizzbuzz" using classic rules.
    :return: A list of strings from 1 to ``to`` with to substitutions made.
    """
    if rules is None:
        rules = create_rules()
    return [FizzBuzzInt(x, rules=rules) for x in range(1, until)]


def _process_rule_arg(arg: str):
    n, word = arg.split('=', 1)
    return make_rule_function(int(n), word)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-u', '--until',
        dest='until',
        type=int,
        default=101,
        help='The number to count up to (exclusive).')
    parser.add_argument(
        '-r', '--rules',
        dest='rules',
        nargs='*',
        type=_process_rule_arg,
        default=None,
        help='Words to substitute for numbers in the form "z=word", '
             'where "z" is the integer for the divisibility test. '
             'If omitted, classic rules will be used.')

    return parser.parse_args(argv)


def main():
    print(*fizzbuzz(**parse_args().__dict__), sep='\n')


if __name__ == '__main__':
    main()
