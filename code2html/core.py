# -*- coding: utf-8 -*-

import sys
import os
import re
from shutil import move
import subprocess

from code2html.vim import get_vimrc, vim_command, clean_vimrc
from code2html.ignores import get_ignores
from code2html.util import get_subdir_name, included, create_subdir, get_shell


vimrc_file = None
pre = False


def fire(args):
    """
    Create Vim configs and then fire up the file traveling.
    """
    global vimrc_file
    vimrc_file = get_vimrc(args.color)

    global pre
    pre = args.pre

    in_out = (args.input, args.output)
    traverse_files(in_out, args.includes)


def traverse_files(in_out, includes):
    """
    Traverse the source directory, and send each file to
    convert. Without lost of the directory structure.
    """
    s_root = in_out[0]
    o_root = in_out[1]

    ignores = get_ignores()  # Apply the ignore list

    for dir_name, sub_dir_name, file_list in os.walk(s_root):
        # Ignore some sub directories, e.g. source code control
        for ig in ignores:
            match = re.search(ig, dir_name, re.IGNORECASE)
            if match:
                break
        else:
            subdir = get_subdir_name(s_root, dir_name)

            if subdir:
                # Create sub directories to preserve the original structure
                create_subdir(o_root, subdir)

            for f in file_list:
                if not included(f, includes):
                    continue  # Only do convert on included files
                if subdir:
                    convert(dir_name, f, os.path.join(o_root, subdir))
                else:
                    convert(dir_name, f, os.path.join(o_root))

    clean_vimrc(vimrc_file)


def convert(source_path, file_name, output_path):
    """
    Call Vim to do the convertion.

    """
    ori_file = os.path.join(source_path, file_name)
    html_file = os.path.join(source_path, file_name + '.html')
    out_file = os.path.join(output_path, file_name + '.html')

    #  Just display, not actually performing the conversion
    print(u'Converting %s into %s' % (ori_file, out_file))

    global pre

    if not pre:
        global vimrc_file
        cmd = vim_command(vimrc_file) + [ori_file]

        try:
            subprocess.call(cmd, shell=get_shell())
            move(html_file, out_file)
        except Exception:
            sys.exit(u'ERROR: Fail to convert files, aborted.')
