#!/usr/bin/env python3

"""
Encrypt or decrypt a text with the Caesar cipher (rotational monoalphabetic substitution cipher), of which ROT13 is a particular case.
"""

__author__  = "Daniele Raffo"
__version__ = "0.1"
__date__    = "3/7/2021"


import argparse
import sys


def parse_command_line():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('key', help = 'Key. Must be an integer from -25 to +25; positive values are used for encryption, negative for decryption. The value 13 (or -13) produces ROT13')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-f', '--file', dest = 'input_filename', type = argparse.FileType('r'), help = 'File containing the input text')
    group.add_argument('-t', '--text', dest = 'input_text', help = 'Input text')
    return parser


def rotate(c, n):
    """Rotate a character by n positions, only if it is an uppercase letter. Takes into account wraparound"""
    if not 65 <= ord(c) <= 90:
        return c
    else:
        m = ord(c) + n
        if m > 90:
            return chr(m - 26)
        elif m < 65:
            return chr(m + 26)
        else:
            return chr(m)    


if __name__ == '__main__':
    args = parse_command_line().parse_args()

    if args.input_text is not None:
        input_text = args.input_text
    elif args.input_filename is not None:
        with args.input_filename as inf:
            input_text = inf.read()

    key = int(args.key)
    if not -25 <= key <= 25:
        print('Key out of range')
        sys.exit()
        
    output_text = ''.join('{}'.format(rotate(c, key)) for c in input_text.upper())

    print(output_text)