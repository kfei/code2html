# -*- coding: utf-8 -*-

import argparse


def get_args():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="the path containing source code")
    p.add_argument("output", help="the path for saving output files")
    p.add_argument("--color", default="default",
                   help="the color scheme to use for syntax highlighting")

    return p.parse_args()
