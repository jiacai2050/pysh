#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import os

import argparse
import shutil
from ..util import stderr_print, extract_args


parser = argparse.ArgumentParser(prog="rm")
parser.add_argument("-r", "--recursive", action="store_true",
                    help="remove directories and their contents recursively")
parser.add_argument("f_or_dirs", nargs="*")


@extract_args
def run(*args):
    if len(args) == 0:
        parser.print_help()
        yield None
    else:
        arg_dict = vars(parser.parse_args(args))
        is_recursive = arg_dict["recursive"]
        f_or_dirs = arg_dict["f_or_dirs"]
        for f_or_dir in f_or_dirs:
            if os.path.exists(f_or_dir):
                if is_recursive:
                    shutil.rmtree(f_or_dir)
                else:
                    if os.path.isdir(f_or_dir):
                        stderr_print("Can't remove a directory[%s] directly, use -r if you like." % f_or_dir)
                    else:
                        os.remove(f_or_dir)
            else:
                stderr_print("%s isn't exists!" % f_or_dir)
            yield None
