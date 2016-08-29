#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import os
from ..util import stderr_print


def run(*args):
    if len(args) == 0:
        stderr_print("touch: missing operand")
        yield None
    else:
        to_touch_files = args[0]
        if isinstance(to_touch_files, basestring):
            to_touch_files = [to_touch_files]
        for to_touch_file in to_touch_files:
            if os.path.exists(to_touch_file):
                os.utime(to_touch_file, None)
                yield None
            else:
                open(to_touch_file, "a").close()
                yield None
