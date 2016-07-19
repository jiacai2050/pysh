#!/usr/bin/env python

import os


def run(*args):
    for d in args:
        os.chdir(d)
        yield os.getcwd()
