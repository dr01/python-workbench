#!/usr/bin/env python3

"""
Generate a page of a book of Borges' Library of Babel
"""

__author__  = "Daniele Raffo"
__version__ = "0.1"
__date__    = "26/10/2018"


from string import ascii_lowercase as _abc
import random


if __name__ == '__main__':

    for i in range(40): print(''.join(random.choices(_abc + ',. ', k = 80)))
