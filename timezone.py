#!/usr/bin/python
import argparse
import shutil

__author__ = 'https://github.com/fejao'

DEFAULT_LAYOUT = "Europe/Berlin"

def __main__(args):

    # import pdb; pdb.set_trace()

    # /etc/timezone
    with open('./wtf', 'r+') as f:
        text = f.read()
        f.seek(0)
        f.write(args.timezone)
        f.truncate()

    # /etc/localtime
    shutil.copy2('/usr/share/zoneinfo/%s' % args.timezone, '/etc/localtime')

# Get the parsed arguments
parser = argparse.ArgumentParser(description='This is script is to be used over the pibakery to change the default timezone')
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
parser.add_argument('-t','--timezone',
    help="The timezone be set('Europe/Amsterdan','Europe/Paris', etc...), default: %s" % DEFAULT_LAYOUT,
    default=DEFAULT_LAYOUT,
    type=str)
args = parser.parse_args()

# RUN
__main__(args)
