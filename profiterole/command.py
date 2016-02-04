'''
Created on 4 Feb 2016

@author: fressi
'''

from __future__ import absolute_import

import sys

import profiterole


_COMMANDS = {}


def main(argv=None):
    'Profit main entry point.'

    if argv is None:
        argv = sys.argv

    if '--version' in argv[1:]:
        print_message(profiterole.__version__)
        return 0

    try:
        command = _COMMANDS[argv[1]]
    except (KeyError, IndexError):
        print_message(
            "Invalid command: {!s}", ' '.join((repr(a) for a in argv[1:])))
        return 1
    else:
        return command(argv)


def print_message(message, *args, **kwargs):
    'Formats and prints a message to standard output.'

    sys.stdout.write((message + '\n').format(*args, **kwargs))


def command(func):
    'Registers a function as a command.'

    assert callable(func)
    _COMMANDS[func.__name__.replace('_', '-')] = func
    return func


@command
def get_sources(argv):
    'get-sources command entry point.'

    return 0
