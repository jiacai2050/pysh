#!/usr/bin/env python

import os


def run(*args):
    pattern = args[0]
    str_or_fs = args[1]
    for str_or_f in str_or_fs:
        if os.path.isfile(str_or_f):
            with open(str_or_f) as f:
                for line in f:
                    line = line.strip()
                    if pattern in line:
                        yield line
        else:
            if pattern in str_or_f:
                yield line
