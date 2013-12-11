# -*- coding: utf-8 -*-

import sys
import re
from subprocess import Popen, PIPE
from os.path import expanduser, isfile, isdir, exists
import glob
from shutil import rmtree
from os import makedirs


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
        sys.exit(u'ERROR: Vim is not yet installed on this system, aborted.')


def check_color_scheme(color):
    """
    Check whether the selected color scheme exists
    TODO: Add Windows support
    """
    if isfile(expanduser('~') + '/.vim/colors/' + color + '.vim'):
        pass  # Color scheme exists
    elif glob.glob('/usr/share/vim/vim*/colors/' + color + '.vim'):
        pass  # Color scheme exists
    else:
        sys.exit(u'ERROR: The selected color scheme does not exist, aborted.')


def test_input(source):
    """
    Test the inupt path
    """
    if isdir(source):
        pass
    else:
        sys.exit(u'ERROR: The source directory does not exist, aborted.')


def test_output(output):
    """
    Test the output path, create it if not exists.
    """
    if exists(output):
        if query_yes_no(u'The output directory exists,'
                        u' delete it first?'):
            rmtree(output)
        else:
            sys.exit(u'Nothing happened.')

    makedirs(output)


def get_subdir_name(root, dir_name):
    regex = '(' + root + ')' + '(.+)'

    match = re.search(regex, dir_name)
    if match:
        subdir_name = match.group(2)[1:]  # Avoid the leading slash
        print regex, dir_name + " => subdir_name: %s" % subdir_name
    else:
        subdir_name = None

    return subdir_name
