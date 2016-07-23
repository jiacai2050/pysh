#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import os


def run(*args):
    for to_touch_file in args:
        if os.path.exists(to_touch_file):
            os.utime(to_touch_file, None)
            yield None
        else:
            open(to_touch_file, "a").close()
            yield None
