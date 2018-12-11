#!/usr/bin/env python3

"""
Compute Fibonacci numbers
"""

__author__  = "Daniele Raffo"
__version__ = "0.1"
__date__    = "10/12/2018"


import argparse
import itertools
import sys


def parse_command_line():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('n', help = 'nth Fibonacci number to compute')
    parser.add_argument('-u', '--upto', action = 'store_true', help = 'Print all Fibonacci numbers up to the nth')
    return parser


def iter_fibonacci():
    """Generator for Fibonacci numbers"""
    (a, b) = (1, 1) 
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci(nth):
    """Get the nth Fibonacci number (from the iterator function)"""
    return next(itertools.islice(iter_fibonacci(), nth - 1, None))




if __name__ == '__main__':
    args = parse_command_line().parse_args()
    number = int(args.n)

    if number < 1:
        print('Error: argument must be a positive integer')
        sys.exit()

    if args.upto:
        for i, fibonacci in zip(range(1, number + 1), iter_fibonacci()): 
            print('{:>4}: {:>4}'.format(i, fibonacci))
    else:
        print(get_fibonacci(number))
