#!/usr/bin/env python3

"""
Demonstrates convergence to the Kaprekar's constant 6174
"""

__author__  = "Daniele Raffo"
__version__ = "0.1"
__date__    = "30/6/2021"


import argparse
import sys
import random


def parse_command_line():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description = __doc__)
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-n', dest = 'nstart', help = 'A positive 4-digit number to start the routine (digits must not be all the same; leading zeros are allowed)')
    group.add_argument('-r', '--random', action = 'store_true', help = 'Runs the Kaprekar\'s routine with a random 4-digit number')
    return parser


def num_to_digitlist(n):
    """Return a List containing the digits of a 4-digit number"""
    s = str(n).zfill(4)
    return [s[0], s[1], s[2], s[3]]


def digitlist_to_num(l):
    """Return a number obtained by concatenating the 4 digits stored in a List"""
    s = [str(i) for i in l]
    return int("".join(s))


def run_kaprekar_routine(n):
    """Run a step of the Kaprekar's routine and return the next number"""
    digits = num_to_digitlist(n)
    nmin = digitlist_to_num(sorted(digits))
    nmax = digitlist_to_num(sorted(digits, reverse=True))
    ndiff = nmax - nmin
    print("{} - {:04d} = {:04d}".format(nmax, nmin, ndiff))
    return ndiff


if __name__ == '__main__':
    args = parse_command_line().parse_args()
    
    if args.nstart:
        number = int(args.nstart)
        if number < 1 or number > 9999:
            print('Error: argument must be a positive 4-digit number')
            sys.exit()   
        digits = num_to_digitlist(number)
        if digits.count(digits[0]) == len(digits):
            print('Error: digits must not be all the same')
            sys.exit() 

    else:
        while True:
            number = random.randrange(1, 9998)
            digits = num_to_digitlist(number)
            if digits.count(digits[0]) != len(digits):
                break
        
    while True:
        number = run_kaprekar_routine(number)        
        if number == 6174:
            break
        
        
        
        
        
    