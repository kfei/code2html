#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from code2html.args import Args
from code2html.util import which
from code2html import core


def main():
    # Exit if Vim is not available
    if which('vim') is None:
        sys.exit(u'ERROR: Vim is not available on this system '
                 u'(maybe a PATH issue), aborted.')

    # Get the arguments passed by user
    args = Args()
    args.check_args()

    # Call Vim to do the conversion
    core.fire(args)

    # Good bye
    sys.exit(0)


if __name__ == '__main__':
    main()
