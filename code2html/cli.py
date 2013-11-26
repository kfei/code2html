#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from code2html.args import get_args
from code2html import util
from code2html import core


if __name__ == '__main__':
    # Get the arguments passed by user
    args = get_args()
    input = util.strip_trailing_slash(args.input)
    output = util.strip_trailing_slash(args.output)
    color = args.color

    # Preparation
    util.check_vim()
    util.check_color_scheme(color)
    util.test_input(input)
    util.test_output(output)

    # List of ignore pattern
    # TODO: Make this configurable
    ignore_list = ['.git', '.svn']

    # Call Vim to do the conversion
    in_out = (input, output)
    core.fire(in_out, ignore_list, color)

    sys.exit(0)
