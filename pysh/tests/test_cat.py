#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from unittest import TestCase, main
from ..builtins import cat
from os import path

script_dir = path.dirname(path.realpath(__file__))


class CatTest(TestCase):

    def setUp(self):
        test_in = path.join(script_dir, "cat.in")
        self.in_file = test_in
        with open(test_in) as f:
            self.in_body = f.readlines()

    def test_cat(self):
        for i, line in enumerate(cat.run(self.in_file)):
            self.assertEqual(self.in_body[i].strip(), line)

        for stdout in cat.run("abc"):
            self.assertEqual("abc", stdout)

if __name__ == "__main__":
    main()
