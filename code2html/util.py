# -*- coding: utf-8 -*-

import sys
import re
import platform
from subprocess import Popen, PIPE
from os.path import expanduser, isfile, isdir, exists, normcase, join
import glob
from shutil import rmtree
from os import makedirs
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


def check_vim():
    """
    Check whether Vim is available
    """
    p1 = Popen(["vim", "--version"], stdout=PIPE)
    p2 = Popen(["grep", "IMproved"], stdin=p1.stdout, stdout=PIPE)
    vim_header = p2.communicate()[0].strip('\n')
    if vim_header:
        pass  # Vim detected
    else:
        sys.exit(u'ERROR: Vim is not available on this system '
                 u'(maybe a PATH issue), aborted.')


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

    makedirs(output)


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
        makedirs(join(o_root, subdir))
    except Exception:
        sys.exit(u'ERROR: Can not create directory, aborted.')
