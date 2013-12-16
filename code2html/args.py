# -*- coding: utf-8 -*-

import argparse


def get_args():
    epilog = ('Example: '
              'code2html --color=jellybeans '
              "--include '*.py' --include 'ext.cpp' "
              "--include '*.h'"
              '/path/to/input /path/to/output')
    p = argparse.ArgumentParser(epilog=epilog)
    p.add_argument('input', help='Path to the source code repository')
    p.add_argument('output', help='Path for saving output files')
    p.add_argument('--color', default='default',
                   help='Specify the color scheme use for syntax highlighting')
    p.add_argument('--include', action='append', dest='includes',
                   default=[],
                   help='Specify file matching patterns, then only the matched'
                        ' files will be convert. Wild card characters are '
                        "supported. e.g. --include='*.c' --include='?.py'")

    return p.parse_args()
