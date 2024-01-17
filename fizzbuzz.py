#!/usr/bin/env python3
"""
FizzBuzz
========

A slightly over-engineered Python implementation of the classic FizzBuzz game.
"""
import argparse
from itertools import starmap
from typing import Callable


def substitute(z: int, word: str) -> Callable[[int], str]:
    """
    Create a function that will return the specified ``word`` if ``n``
    divides ``z`` evenly. Otherwise, return an empty string.

    :param z: The divisor.
    :param word: The word to be substituted.
    """
    def sub(n: int) -> str:
        return word if n % z == 0 else ''

    return sub


def fizzbuzz(to: int = 101,
             substitutions: list[tuple[int, str]] | None = None) -> list[str]:
    """
    Play the FizzBuzz game.

    :param to: The number to count up to (exclusive).
    :param substitutions: A list of tuples. Each tuple should contain an integer
            for the divisibility test followed by the word that should replace
            the number if it passes the divisibility test. If ``None`` is given,
            classic FizzBuzz rules using 3 and 5 are used. Words are stacked
            such that the number 15 will yield "fizzbuzz" using classic rules.
    :return: A list of strings from 1 to ``to`` with to substitutions made.
    """
    if substitutions is None:
        substitutions = [(3, 'fizz'), (5, 'buzz')]
    subs = list(starmap(substitute, substitutions))
    return [''.join(s(x) for s in subs) or str(x) for x in range(1, to)]


def _process_substitution_arg(arg: str):
    n, word = arg.split('=', 1)
    return int(n), word


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-t', '--to',
        dest='to',
        type=int,
        default=101,
        help='The number to count up to (exclusive).')
    parser.add_argument(
        '-s', '--substitute',
        dest='substitutions',
        nargs='*',
        type=_process_substitution_arg,
        default=None,
        help='Words to substitute for numbers in the form "z=word", '
             'where "z" is the integer for the divisibility test. '
             'If omitted, classic rules will be used.')

    return parser.parse_args(argv)


def main():
    print(*fizzbuzz(**parse_args().__dict__), sep='\n')


if __name__ == '__main__':
    main()
