# -*- coding: utf-8 -*-

import unittest

from code2html.util import get_subdir_name, included


class GetSubdirNameTest(unittest.TestCase):
    def test_root_starts_with_dot(self):
        root = '.'
        dir_name = './first/second'
        self.assertEqual(get_subdir_name(root, dir_name), 'first/second')

    def test_root_starts_with_wave(self):
        root = '~'
        dir_name = '~/first/second/third'
        self.assertEqual(get_subdir_name(root, dir_name), 'first/second/third')


class IncludedTest(unittest.TestCase):
    def test_with_star_wildcard_matching(self):
        f = 'source_code.py'
        includes = ['*.py']
        self.assertTrue(included(f, includes))

    def test_with_question_mark_wildcard_matching(self):
        f1 = 'source_code.py'
        f2 = 's.py'
        includes = ['?.py']

        t1 = included(f1, includes)
        t2 = included(f2, includes)

        self.assertEqual((t1, t2), (False, True))
