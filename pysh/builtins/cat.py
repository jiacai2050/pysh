#!/usr/bin/env python

import os


def run(*args):
    for grep_f in args:
        if os.path.isfile(grep_f):
            with open(grep_f) as f:
                for line in f:
                    yield line.strip()
        else:
            yield grep_f
