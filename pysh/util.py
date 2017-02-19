#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import sys
import codecs
import itertools
from chardet.universaldetector import UniversalDetector


def stderr_print(msg):
    if isinstance(msg, unicode):
        msg = msg.encode("utf-8")
    print(msg, file=sys.stderr)


def generalize_args(func):
    """
    the last one of a commands args can be a:
    1. string (normal)
    2. generator (pipeline)

    This annotation is used for turning the string arg(case 1) into a iterable object, List for now.
    """
    def wrapper(*args):
        if 0 == len(args):
            full_args = []
        else:
            full_args = [arg for arg in args[0:-1]]

            if isinstance(args[-1], basestring):
                full_args.append([args[-1]])
            else:
                full_args = itertools.chain(full_args, args[-1])
        return func(*full_args)

    return wrapper


def guess_file_encoding(guess_file, detector=UniversalDetector()):
    max_guess, current_guess = 10, 1
    good_guess = False
    default_encoding = "utf-8"
    detector.reset()
    with open(guess_file, "rb") as f:
        for line in f:
            if current_guess == max_guess:
                break
            else:
                current_guess += 1

            detector.feed(line)
            if detector.done:
                good_guess = True
                break

    detector.close()

    return detector.result["encoding"] if good_guess else default_encoding


def open_file(file_to_open):
    file_encoding = guess_file_encoding(file_to_open)
    with codecs.open(file_to_open, encoding=file_encoding) as f:
        for line in f:
            yield line
