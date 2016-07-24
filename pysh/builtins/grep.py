#!/usr/bin/env python

import os
from ..util import open_file, extract_args


@extract_args
def run(*args):
    pattern = args[0]
    str_or_fs = args[1:]

    for str_or_f in str_or_fs:
        if os.path.isfile(str_or_f):
            for line in open_file(str_or_f):
                if pattern in line:
                    yield line.strip()
        else:
            if pattern in str_or_f:
                yield str_or_f


if __name__ == '__main__':
    for line in run("python", "grep.py"):
        print(line)
