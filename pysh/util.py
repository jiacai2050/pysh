#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import sys
from glob import glob


def stderr_print(msg):
    print(msg, file=sys.stderr)


def expand_wildcard_args(func):
    def wrapper(*args, **kw):
        cmd_name, cmd_args = func(*args, **kw)

        if cmd_args is not None and len(cmd_args) > 0:
            expanded_args = []
            for arg in cmd_args:
                matched_items = glob(arg)
                if len(matched_items) == 0:
                    expanded_args.append(arg)
                else:
                    expanded_args += matched_items
            return cmd_name, expanded_args
        else:
            return cmd_name, cmd_args

    return wrapper
