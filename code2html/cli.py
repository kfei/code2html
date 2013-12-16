#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os.path import normpath

from code2html.args import get_args
from code2html import util
from code2html import core


def main():
    # Get the arguments passed by user
    args = get_args()
    input = normpath(args.input)
    output = normpath(args.output)
    includes = args.includes
    color = args.color

    # Preparation
    util.check_vim()
    util.check_color_scheme(color)
    util.test_input(input)
    util.test_output(output)
    util.test_includes(includes)

    # Call Vim to do the conversion
    core.fire(input, output, includes, color)

    sys.exit(0)


if __name__ == '__main__':
    main()
