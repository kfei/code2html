# -*- coding: utf-8 -*-

import argparse


def get_args():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="path to the source code repository")
    p.add_argument("output", help="path for saving output files")
    p.add_argument("--color", default="default",
                   help="the color scheme to use for syntax highlighting")

    return p.parse_args()
