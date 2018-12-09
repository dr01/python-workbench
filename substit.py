#!/usr/bin/env python3

"""
Encrypt or decrypt text with a monoalphabetic substitution cipher
"""

__author__  = "Daniele Raffo"
__version__ = "0.2"
__date__    = "2/12/2018"


import argparse
import sys


def parse_command_line():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description = __doc__)
    group1 = parser.add_mutually_exclusive_group(required = True)
    group1.add_argument('-e', '--encrypt', action = 'store_true', help = 'Encrypt text passed as input')
    group1.add_argument('-d', '--decrypt', action = 'store_true', help = 'Decrypt text passed as input')
    group2 = parser.add_mutually_exclusive_group(required = True)
    group2.add_argument('-f', '--file', dest = 'input_filename', type = argparse.FileType('r'), help = 'File containing the input text')
    group2.add_argument('-t', '--text', dest = 'input_text', help = 'Input text')
    parser.add_argument('-k', '--key', dest = 'key_filename', type = argparse.FileType('r'), default = 'substit.key',
                        help = 'File containing the key; if not specified, uses substit.key')
    return parser


if __name__ == '__main__':
    args = parse_command_line().parse_args()

    # Get key
    key = {}
    n_keys = 0
    with args.key_filename as kf:
        line = kf.readline().strip()
        while line:
            key[line[0]] = line[2]
            n_keys += 1
            line = kf.readline().strip()

    # Verify uniqueness of elements in the key
    if len(key) < n_keys:
        print('Bad key: multiple replacement definitions ({}) for the same letter'.format(n_keys - len(key)))
        sys.exit()

    # Invert key (to verify that replacements are unique, and for decryption)
    inverted_key = {v: k for k, v in key.items()}
    if len(inverted_key) < len(key):
        print('Bad key: some letters with identical replacements ({} dupes), encryption would produce ambiguous text'.format(len(key) - len(inverted_key)))
        sys.exit() 

    # Get input text from given source
    if args.input_text is not None:
        input_text = args.input_text
    elif args.input_filename is not None:
        with args.input_filename as inf:
            input_text = inf.read()

    # Encrypt or decrypt text
    if args.encrypt:
        output_text = ''.join('{}'.format(key.get(c, c)) for c in input_text.lower())
    elif args.decrypt:
        output_text = ''.join('{}'.format(inverted_key.get(c, c)) for c in input_text)    

    print(output_text)

