# -*- coding: utf-8 -*-

import argparse
from os.path import normpath

from code2html.util import (check_color_scheme,
                            check_input,
                            check_output,
                            check_includes)


class Args():
    def __init__(self):
        args = self.get_args()
        self.input = normpath(args.input)
        self.output = normpath(args.output)
        self.includes = args.includes
        self.color = args.color
        self.pre = args.pre

    def get_args(self):
        epilog = ('Example: '
                  'code2html --color=jellybeans '
                  "--include '*.py' --include 'ext.cpp' "
                  "--include '*.h'"
                  '/path/to/input /path/to/output')

        p = argparse.ArgumentParser(epilog=epilog)

        p.add_argument('input', help='Path to the source code repository')

        p.add_argument('output', help='Path for saving output files')

        p.add_argument('--color', default='default',
                       help='Specify the color scheme use for syntax'
                            'highlighting')

        p.add_argument('--include', action='append', dest='includes',
                       default=[],
                       help='Specify file matching patterns, then only the '
                            'matched files will be convert. Wild card '
                            'characters are supported. '
                            "e.g. --include='*.c' --include='?.py'")

        p.add_argument('--pre', action='store_true', dest='pre',
                       help='Instead of actually performing the conversion, '
                            'simply display what *would* have been converted '
                            "if --pre weren't used")

        return p.parse_args()

    def check_args(self):
        check_color_scheme(self.color)
        check_input(self.input)
        check_output(self.output)
        check_includes(self.includes)
