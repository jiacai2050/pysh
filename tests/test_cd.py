#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from pysh.builtins import cd
from os import path


def test_cd():
    home_dir = path.expanduser("~")
    ret = cd.run(home_dir)
    assert home_dir == next(ret)
