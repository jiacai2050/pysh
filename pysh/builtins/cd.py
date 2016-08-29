#!/usr/bin/env python

import os


def run(*args):
    if len(args) == 0:
        os.chdir(os.path.expanduser("~"))
        yield os.getcwd()
    else:
        dirs = args[0]
        if isinstance(dirs, basestring):
            dirs = [dirs]
        for d in dirs:
            os.chdir(d)
            yield os.getcwd()
