#!/usr/bin/env python

import os
import types


def run(*args):
    pattern = args[0]
    if isinstance(args[1], types.GeneratorType):
        str_or_fs = args[1]
    else:
        str_or_fs = args[1:]
    for str_or_f in str_or_fs:
        if os.path.isfile(str_or_f):
            with open(str_or_f) as f:
                for line in f:
                    line = line.strip()
                    if pattern in line:
                        yield line
        else:
            if pattern in str_or_f:
                yield str_or_f


if __name__ == '__main__':
    for line in run("python", "grep.py"):
        print(line)
