'''
Created on 4 Feb 2016

@author: fressi
'''

from __future__ import absolute_import

import sys

import profiterole


def main(argv=None):
    'Profit main entry point.'

    if argv is None:
        argv = sys.argv

    sys.stdout.write(profiterole.__version__ + '\n')
    return 0
