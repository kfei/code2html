#!/usr/bin/env python
# -*- coding: utf-8 -*-

from args import get_args

import util
import core


if __name__ == '__main__':
    # Get the arguments passed by user
    args = get_args()
    SOURCE = util.strip_trailing_slash(args.source)
    OUTPUT = util.strip_trailing_slash(args.output)
    COLOR = args.color

    # Preparation
    util.check_vim()
    util.check_color_scheme(COLOR)
    util.test_input(SOURCE)
    util.test_output(OUTPUT)

    # List of ignore pattern
    # TODO: Make this configurable
    ignore_list = ['.git', '.svn']

    # Call Vim to do the conversion
    in_out = (SOURCE, OUTPUT)
    core.traverse_files(in_out, ignore_list)
