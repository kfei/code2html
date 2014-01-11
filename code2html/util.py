# -*- coding: utf-8 -*-

import sys
import re
import os
import platform
from os.path import expanduser, isfile, isdir, exists, normcase, join
import glob
from shutil import rmtree
from fnmatch import fnmatch


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes": True, "y": True,  "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            pass


def which(program):
    """
    Check if an executable program exists, in a platform-independent way.
    Idea comes from: http://stackoverflow.com/a/377028/2504317
    """
    if platform.system() == 'Windows':
        program += '.exe'

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def check_color_scheme(color):
    """
    Check whether the selected color scheme exists
    """
    if platform.system() == 'Windows':
        user_cs_file = normcase(join(expanduser('~'),
                                     'vimfiles/colors', color + '.vim'))
        builtin_cs_file = normcase('C:/Program Files*/Vim/vim*/colors/'
                                   + color + '.vim')
    else:
        user_cs_file = expanduser('~') + '/.vim/colors/' + color + '.vim'
        builtin_cs_file = '/usr/share/vim/vim*/colors/' + color + '.vim'

    if isfile(user_cs_file):
        pass  # Color scheme exists
    elif glob.glob(builtin_cs_file):
        pass  # Color scheme exists
    else:
        sys.exit(u'ERROR: The selected color scheme does not exist, aborted.')


def check_input(source):
    """
    Check the inupt path
    """
    if isdir(source):
        pass
    else:
        sys.exit(u'ERROR: The source directory does not exist, aborted.')


def check_output(output):
    """
    Check the output path, create it if not exists.
    """
    if exists(output):
        if query_yes_no(u'The output directory exists,'
                        u' delete it first?'):
            rmtree(output)
        else:
            sys.exit(u'Nothing happened.')

    os.makedirs(output)


def check_includes(includes):
    """
    Stop program if there is no include pattern
    """
    if includes == []:
        sys.exit(u'No include pattern specified, aborted.')


def get_subdir_name(root, dir_name):
    regex = '(' + root + ')' + '(.+)'

    match = re.search(regex, dir_name)
    if match:
        subdir_name = match.group(2)[1:]  # Avoid the leading slash
    else:
        subdir_name = None

    return subdir_name


def included(f, includes):
    for pattern in includes:
        if fnmatch(f, pattern):
            return True

    return False


def create_subdir(o_root, subdir):
    print(u'Making directory %s' %
          join(o_root, subdir))
    try:
        os.makedirs(join(o_root, subdir))
    except Exception:
        sys.exit(u'ERROR: Can not create directory, aborted.')


def get_shell():
    """
    For Windows, the shell flag in subprocess.call must be True.
    FIXME: Find a more general way.
    """
    if platform.system() == 'Windows':
        return True
    else:
        return False
