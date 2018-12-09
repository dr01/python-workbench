#!/usr/bin/env python3

"""
Print number of occurrences and frequency of letters in a text
"""

__author__  = "Daniele Raffo"
__version__ = "0.1"
__date__    = "14/10/2018"


import argparse
from string import ascii_lowercase as _alphabet
from collections import Counter as _Counter


def parse_command_line():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description = __doc__)
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-f', '--file', dest = 'input_filename', type = argparse.FileType('r'), help = 'File containing the text to analyze')
    group.add_argument('-t', '--text', dest = 'input_text', help = 'Text to analyze')
    parser.add_argument('-n', '--nonulls', action = 'store_true', help = 'Hide letters with zero frequency')
    parser.add_argument('-o', '--total', action = 'store_true', help = 'Include total number of characters and letters')
    parser.add_argument('-s', '--sortfreq', action = 'store_true', help = 'Sort by letter frequency, highest first')
    return parser


if __name__ == '__main__':
    args = parse_command_line().parse_args()

    # Get input text from chosen source
    if args.input_text is not None:
        text = args.input_text
    elif args.input_filename is not None:
        with args.input_filename as filename:
            text = filename.read()

    # Analyze input text
    frequency = _Counter({c: 0 for c in _alphabet})
    frequency.update(c for c in text.lower() if c in frequency)
    total_letters = sum(frequency.values())
    total_chars = len(text.replace('\n', ''))   # do not count newline chars

    # Output results
    if not args.sortfreq:
        output = sorted(frequency.items(), key = lambda x: x[0], reverse = False)        
    else:
        output = sorted(frequency.items(), key = lambda x: x[1], reverse = True)
    for c, n in output:
        if not (args.nonulls and n == 0):
            print('{}:{:>8}{:10.2f}%'.format(c, n, 100 * n / (total_letters or 1)))
    if args.total:
        print('Total letters:   {:>8}\nTotal characters:{:>8}'.format(total_letters, total_chars))
