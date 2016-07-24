#!/usr/bin/env python

import os
import types


def run(*args):
    if len(args) == 0:
        os.chdir(os.path.expanduser("~"))
        yield os.getcwd()
    else:
        if isinstance(args[0], types.GeneratorType):
            dirs = args[0]
        else:
            dirs = args

        for d in dirs:
            os.chdir(d)
            yield os.getcwd()
