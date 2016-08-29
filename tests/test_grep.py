#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from os import path
from pysh.builtins import grep

script_dir = path.dirname(path.realpath(__file__))


def test_grep():
    test_in = path.join(script_dir, "grep.in")
    wanteds = ["aaa", "aab", "aac"]
    ret = grep.run("aa", [test_in])
    ret2 = grep.run("aa", test_in)
    for wanted in wanteds:
        assert next(ret) == wanted
        assert next(ret2) == wanted
