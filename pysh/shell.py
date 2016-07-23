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
            piped_cmds = parser.tokens2piped_cmd(tokens)
            shell_proc = parser.assemble(piped_cmds)
            for stdout in shell_proc.run():
                if stdout is not None:
                    print(stdout)


def main():
    shell_loop()

if __name__ == "__main__":
    main()
