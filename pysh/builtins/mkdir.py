#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import os
from ..util import stderr_print


def run(*dirs):
    if len(dirs) == 0:
        stderr_print("mkdir: missing operand")
        yield None
    else:
        for dir in dirs:
            if os.path.exists(dir):
                stderr_print("mkdir: cannot create directory [%s]: File exists" % dir)
                yield None
            else:
                os.makedirs(dir)
                yield None
