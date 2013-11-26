# -*- coding: utf-8 -*-

import sys
import os
import re
from shutil import move
import subprocess

from code2html.vim import get_vimrc, vim_command, clean_vimrc


vimrc_file = None


def fire(in_out, ignore_list, color):
    """
    Create Vim configs and then fire up the file traveling.
    """
    global vimrc_file
    vimrc_file = get_vimrc(color)
    traverse_files(in_out, ignore_list)


def traverse_files(in_out, ignore_list):
    """
    Traverse the source directory, and send each file to
    convert. Without lost of the directory hierachy.
    """
    s_root = in_out[0]  # The source directory
    o_root = in_out[1]  # The output directory

    for dir_name, sub_dir_name, file_list in os.walk(s_root):
        for ig in ignore_list:
            match = re.search(ig, dir_name, re.IGNORECASE)
            if match:
                break
        else:
            # FIXME: Must find a better way to deal with slashes
            regex = '(' + s_root + ')' + r'(.*)'
            match = re.search(regex, dir_name)
            if match:
                subdir = match.group(2)[1:]  # Avoid the leading slash
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
