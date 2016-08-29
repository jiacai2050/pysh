#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import os
from ..util import stderr_print


def run(*args):
    if len(args) == 0:
        for f_or_dir in os.listdir(os.getcwd()):
            yield f_or_dir
    else:
        f_or_dirs = args[0]
        if isinstance(f_or_dirs, basestring):
            f_or_dirs = [f_or_dirs]

        for f_or_dir in f_or_dirs:
            if os.path.exists(f_or_dir):
                if os.path.isfile(f_or_dir):
                    yield f_or_dir
                else:
                    for sub_f_or_dir in os.listdir(f_or_dir):
                        yield sub_f_or_dir
            else:
                stderr_print("%s doesn't exists" % f_or_dir)
                yield None
