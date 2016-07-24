#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import sys
import codecs
import types
from glob import glob
from chardet.universaldetector import UniversalDetector


def stderr_print(msg):
    if isinstance(msg, unicode):
        msg = msg.encode("utf-8")
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


def extract_args(func):
    """
    the last one of a commands args can be:
    1. a string (normal)
    2. generator (pipeline)

    This annotation is used for extract args out of a generator
    """
    def wrapper(*args):
        if 0 == len(args):
            full_args = []
        else:
            partial_args = [arg for arg in args[0:-1]]
            extracted_args = []
            if isinstance(args[-1], types.GeneratorType):
                for arg in args[-1]:
                    extracted_args.append(arg)
            else:
                extracted_args.append(args[-1])

            full_args = partial_args + extracted_args

        return func(*full_args)

    return wrapper


detector = UniversalDetector()


def open_file(file_to_open):
    detector.reset()

    with open(file_to_open, "rb") as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break

    detector.close()
    file_encoding = detector.result["encoding"]

    with codecs.open(file_to_open, encoding=file_encoding) as f:
        for line in f:
            yield line
