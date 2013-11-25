# -*- coding: utf-8 -*-

import os
import re
from shutil import move
# import subprocess


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
                    print('Making directory %s' % o_root + '/' + subdir)
                    try:
                        os.makedirs(os.path.join(o_root, subdir))
                    except Exception:
                        print('ERROR')

            for f in file_list:
                if subdir:
                    convert(dir_name, f, os.path.join(o_root, subdir))
                else:
                    convert(dir_name, f, os.path.join(o_root))


def convert(source_path, file_name, output):
    """
    Vim command:
        for i in *.ext; do vim -c TOhtml -c wqa $i ; done
        OR
        for f in *.[ch]; do
            gvim -f +"syn on" +"run! syntax/2html.vim" +"wq" +"q" $f;
        done
    """
    ori_file = os.path.join(source_path, file_name)
    print('Converting %s into %s' % (ori_file, output))
    try:
        move(ori_file, output)
    except Exception:
        print('ERROR')
