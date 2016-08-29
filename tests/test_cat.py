#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from os import path
from pysh.builtins import cat

script_dir = path.dirname(path.realpath(__file__))


def test_cat():
    test_in = path.join(script_dir, "cat.in")

    ret = cat.run(test_in)
    wanteds = ["aaa", "bbb", "ccc"]
    for wanted in wanteds:
        assert next(ret) == wanted

    for stdout in cat.run("abc"):
        assert "abc" == stdout
