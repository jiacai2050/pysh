#!/usr/bin/env python

import os
from ..util import open_file


def run(*args):
    for grep_f in args:
        if os.path.isfile(grep_f):
            for line in open_file(grep_f):
                yield line.strip()
        else:
            yield grep_f
