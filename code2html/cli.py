#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from args import get_args
from subprocess import Popen, PIPE
from os.path import expanduser, isfile, isdir, exists
from os import makedirs
from shutil import rmtree
import glob

from utils import query_yes_no


if __name__ == '__main__':
    # Get the arguments passed by user
    args = get_args()

    # Check whether Vim is available
    p1 = Popen(["vim", "--version"], stdout=PIPE)
    p2 = Popen(["grep", "IMproved"], stdin=p1.stdout, stdout=PIPE)
    vim_header = p2.communicate()[0].strip('\n')
    if vim_header:
        pass  # Vim detected
    else:
        sys.exit(u'ERROR: Vim is not yet installed on this system, aborted.')

    # Check whether the selected color scheme exists
    # TODO: Add Windows support
    if isfile(expanduser('~') + '/.vim/colors/' + args.color + '.vim'):
        pass  # Color scheme exists
    elif glob.glob('/usr/share/vim/vim*/colors/' + args.color + '.vim'):
        pass  # Color scheme exists
    else:
        sys.exit(u'ERROR: The selected color scheme does not exist, aborted.')

    # Test the inupt path
    if isdir(args.source):
        pass
    else:
        sys.exit(u'ERROR: The source directory does not exist, aborted.')

    # Test the output path
    if exists(args.output):
        if query_yes_no(u'The output directory exists, delete it first?'):
            rmtree(args.output)
        else:
            sys.exit(u'Nothing happened.')

    makedirs(args.output)

    # TODO: Call Vim to do the conversion
