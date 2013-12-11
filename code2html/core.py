# -*- coding: utf-8 -*-

import sys
import os
import re
from shutil import move
import subprocess
from fnmatch import fnmatch

from code2html.vim import get_vimrc, vim_command, clean_vimrc
from code2html.filter import get_filter
from code2html.util import get_subdir_name


vimrc_file = None


def fire(in_out, color):
    """
    Create Vim configs and then fire up the file traveling.
    """
    global vimrc_file
    vimrc_file = get_vimrc(color)
    traverse_files(in_out)


def traverse_files(in_out):
    """
    Traverse the source directory, and send each file to
    convert. Without lost of the directory hierachy.
    """
    s_root = in_out[0]
    o_root = in_out[1]

    filter = get_filter()  # Apply the ignore list

    for dir_name, sub_dir_name, file_list in os.walk(s_root):
        # Ignore some sub directories, e.g. source code control
        for ig in filter:
            match = re.search(ig, dir_name, re.IGNORECASE)
            if match:
                break
        else:
            # Create sub directories to preserve the original structure
            subdir = get_subdir_name(s_root, dir_name)
            if subdir:
                print(u'Making directory %s' %
                      os.path.join(o_root, subdir))
                try:
                    os.makedirs(os.path.join(o_root, subdir))
                except Exception:
                    sys.exit(u'ERROR: Can not create directory, aborted.')

            for f in file_list:
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

    global vimrc_file

    print(u'Converting %s into %s' % (ori_file, out_file))

    cmd = vim_command(vimrc_file) + [ori_file]

    try:
        subprocess.call(cmd)
        move(html_file, out_file)
    except Exception:
        sys.exit(u'ERROR: Fail to convert files, aborted.')
