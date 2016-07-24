#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from unittest import TestCase, main
from os import path
from ..builtins import cat

script_dir = path.dirname(path.realpath(__file__))


class CatTest(TestCase):

    def setUp(self):
        self.test_in = path.join(script_dir, "cat.in")
        self.wanted = ["aaa", "bbb", "ccc"]

    def test_cat(self):
        for i, line in enumerate(cat.run(self.test_in)):
            self.assertEqual(self.wanted[i], line)

        for stdout in cat.run("abc"):
            self.assertEqual("abc", stdout)

if __name__ == "__main__":
    main()
