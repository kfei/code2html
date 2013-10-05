#!/usr/bin/env python
# -*- coding: utf-8 -*-

from args import get_args

import utils


if __name__ == '__main__':
    # Get the arguments passed by user
    args = get_args()

    # Preparation
    utils.check_vim()
    utils.check_color_scheme(args.color)
    utils.test_input(args.source)
    utils.test_output(args.output)

    # TODO: Call Vim to do the conversion
