#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from code2html.args import Args
from code2html.util import check_vim
from code2html import core


def main():
    # Preparation
    check_vim()

    # Get the arguments passed by user
    args = Args()
    args.check_args()

    # Call Vim to do the conversion
    core.fire(args)

    # Good bye
    sys.exit(0)


if __name__ == '__main__':
    main()
