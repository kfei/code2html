#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from args import get_args
from subprocess import Popen, PIPE

if __name__ == '__main__':
    # Get the arguments passed by user
    args = get_args()
    
    # Check whether Vim is available 
    p1 = Popen(["vim", "--version"], stdout=PIPE)
    p2 = Popen(["grep", "IMproved"], stdin=p1.stdout, stdout=PIPE)
    vim_header = p2.communicate()[0].strip('\n')
    if vim_header:
        pass # Vim detected
    else:
        sys.exit(u'ERROR: Vim is not yet installed on this system, aborted.')

    # TODO: Arguments validation

    # TODO: Test the inupt/output directories

    # TODO: Call Vim to do the conversion
