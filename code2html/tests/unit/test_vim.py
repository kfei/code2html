# -*- coding: utf-8 -*-

import unittest

from code2html.vim import vim_command


class VimCommandTest(unittest.TestCase):
    def test_vim_command(self):
        vimrc_file = '/tmp/temporary-vimrc'
        expected = 'vim -u /tmp/temporary-vimrc -c TOhtml -c wqa'
        self.assertEqual(expected, ' '.join(vim_command(vimrc_file)))
