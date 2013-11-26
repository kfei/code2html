# -*- coding: utf-8 -*-

import sys
import tempfile
import os
from os.path import expanduser


def get_vimrc(color='default'):
    base = ("set nocompatible\n"
            "set t_Co=256\n"
            "syntax on\n"
            "set encoding=utf-8\n"
            "set ai\n"
            "set tabstop=4 shiftwidth=4 softtabstop=4\n"
            "set expandtab\n"
            "filetype plugin on\n"
            "filetype indent on\n")

    color_scheme = "colorscheme %s\n" % color
    config = base + color_scheme

    try:
        with tempfile.NamedTemporaryFile(dir=expanduser('~'),
                                         delete=False) as t:
            t.write(config)
            t.flush()
            vimrc_file = t.name

    except Exception:
        sys.exit(u'ERROR: Can not create temporary .vimrc, aborted.')

    return vimrc_file


def vim_command(vimrc_file):
    vim_cmd = ['vim', '-u', vimrc_file, '-c', 'TOhtml', '-c', 'wqa']
    return vim_cmd


def clean_vimrc(vimrc_file):
    try:
        os.remove(vimrc_file)
    except Exception:
        print(u'WARN: Can not clean the temporary .vimrc file.')
