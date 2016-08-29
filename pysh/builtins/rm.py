#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import os

import argparse
import shutil
from ..util import stderr_print


parser = argparse.ArgumentParser(prog="rm")
parser.add_argument("-r", "--recursive", action="store_true",
                    help="remove directories and their contents recursively")
parser.add_argument("f_or_dirs", nargs="*")


def run(*args):
    if len(args) == 0:
        parser.print_help()
        yield None
    else:
        # arg_dict = vars(parser.parse_args(args))
        # is_recursive = arg_dict["recursive"]
        # f_or_dirs = arg_dict["f_or_dirs"]

        f_or_dirs = args[0]
        if isinstance(f_or_dirs, basestring):
            f_or_dirs = [f_or_dirs]

        for f_or_dir in f_or_dirs:
            if os.path.exists(f_or_dir):
                if os.path.isdir(f_or_dir):
                    shutil.rmtree(f_or_dir)
                else:
                    os.remove(f_or_dir)
            else:
                stderr_print("%s isn't exists!" % f_or_dir)
            yield None
