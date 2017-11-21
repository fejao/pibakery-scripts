#!/usr/bin/python

import argparse

__author__ = 'https://github.com/fejao'

DEFAULT_LAYOUT = 'de'

def __main__(args):

    f = open('/etc/default/keyboard', 'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace("gb", DEFAULT_LAYOUT)

    f = open('/etc/default/keyboard', 'w')
    f.write(newdata)
    f.close()

# Get the parsed arguments
parser = argparse.ArgumentParser(description='This is script is to be used over the pibakery to change the default keyboard layout')
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
parser.add_argument('-k','--keyboard-layout',
    help="The keyboard layout to be set('us','fr', etc...), default: %s" % DEFAULT_LAYOUT,
    default=DEFAULT_LAYOUT
    type=str)
args = parser.parse_args()

# RUN
__main__(args)
