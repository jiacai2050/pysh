#!/usr/bin/env python

import os
import types
from ..util import open_file


def run(*args):
    pattern = args[0]
    if isinstance(args[1], types.GeneratorType):
        str_or_fs = args[1]
    else:
        str_or_fs = args[1:]
    for str_or_f in str_or_fs:
        if os.path.isfile(str_or_f):
            for line in open_file(str_or_f):
                yield line.strip()
        else:
            if pattern in str_or_f:
                yield str_or_f


if __name__ == '__main__':
    for line in run("python", "grep.py"):
        print(line)
