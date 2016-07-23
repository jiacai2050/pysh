#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import importlib
from glob import glob
from os import path, sep
from ..util import stderr_print


builtins = {}

py_path = path.dirname(path.realpath(__file__))

for py_file in glob("%s%s*.py" % (py_path, sep)):
    py_file = py_file.split(sep)[-1]
    if py_file.startswith("__"):
        pass
    else:
        try:
            cmd_name, _ = path.splitext(py_file)
            cmd_runner = importlib.import_module(".%s" % cmd_name, __name__).run
            builtins[cmd_name] = cmd_runner
        except Exception as e:
            stderr_print("load builtin cmd[%s] error: %s" % (cmd_name, e))


__all__ = ["builtins"]
