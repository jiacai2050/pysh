#!/usr/bin/env python

import os
from ..util import extract_args


@extract_args
def run(*args):
    if len(args) == 0:
        os.chdir(os.path.expanduser("~"))
        yield os.getcwd()
    else:
        dirs = args
        for d in dirs:
            os.chdir(d)
            yield os.getcwd()
