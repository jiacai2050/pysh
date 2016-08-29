#!/usr/bin/env python

import os
from ..util import open_file, stderr_print


def run(*args):
    if len(args) == 0:
        stderr_print("cat: missing one param")
        yield None
    else:
        f_or_strs = args[0]
        if isinstance(f_or_strs, basestring):
            f_or_strs = [f_or_strs]

        for f_or_str in f_or_strs:
            if os.path.isfile(f_or_str):
                for line in open_file(f_or_str):
                    yield line.strip()
            else:
                yield f_or_str
