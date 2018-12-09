#!/usr/bin/env python3

"""
Convert a string into HTML entities
"""

__author__  = "Daniele Raffo"
__version__ = "0.1"
__date__    = "07/10/2018"    


import argparse


def parse_command_line():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('string_to_mung', help = 'String to convert')
    parser.add_argument('-l', '--link', action = 'store_true', help = 'Embed the munged string into a mailto: link')
    return parser


def mung(plain):
    """Convert each character of a string into its HTML entity"""  
    return ''.join('&#{};'.format(ord(c)) for c in plain)


if __name__ == '__main__':
    args = parse_command_line().parse_args()
    if not args.link:
        string_munged = mung(args.string_to_mung)
    else:
        string_munged = '<a href="{0}{1}">{1}</a>'.format(mung('mailto:'), mung(args.string_to_mung)) 
    print(string_munged)
