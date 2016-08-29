#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from . import parser


def shell_loop():
    while True:
        line = raw_input("> ")
        if line != "":
            tokens = parser.tokenize(line)
            cmds = parser.tokens2cmds(tokens)
            shell_proc = parser.assemble(cmds)
            shell_proc.run()


def main():
    shell_loop()

if __name__ == "__main__":
    main()
