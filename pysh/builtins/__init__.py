#!/usr/bin/env python

import importlib
from glob import glob
from os import path, sep
import sys


builtins = {}

py_path = path.dirname(path.realpath(__file__))

for py_file in glob("%s%s*.py" % (py_path, sep)):
    py_file = py_file.split(sep)[-1]
    if py_file.startswith("__"):
        pass
    else:
        try:
            func_name, _ = path.splitext(py_file)
            func = importlib.import_module(".%s" % func_name, __name__).run
            builtins[func_name] = func
        except Exception, e:
            print >> sys.stderr, "load builtin func[%s] error: %s" % (func_name, e)


__all__ = ["builtins"]
