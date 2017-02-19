#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from . import interpreter
from .ShellProcessor import ShellProcessor


def shell_loop():
    while True:
        line = raw_input("> ")
        if line != "":
            tokens = interpreter.tokenize(line)
            cmds = interpreter.analyze(tokens)
            ShellProcessor(cmds).run()


def main():
    shell_loop()

if __name__ == "__main__":
    main()
