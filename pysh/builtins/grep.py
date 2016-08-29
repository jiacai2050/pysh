#!/usr/bin/env python

import os
from ..util import open_file


def run(*args):
    pattern = args[0]
    str_or_fs = args[1]
    if isinstance(str_or_fs, basestring):
        str_or_fs = [str_or_fs]
    for str_or_f in str_or_fs:
        if os.path.isfile(str_or_f):
            for line in open_file(str_or_f):
                if pattern in line:
                    yield line.strip()
        else:
            if pattern in str_or_f:
                yield str_or_f
