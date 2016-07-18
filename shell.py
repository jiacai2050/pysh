#!/usr/bin/env python

import os
import shlex
from .constants import SHELL_STATUS_RUN
from .builtins import builtins


def tokenize(line):
    return shlex.split(line)


def execute(cmd_tokens):

    if cmd_tokens[0] in builtins:
        return builtins[cmd_tokens[0]](cmd_tokens[1:])

    pid = os.fork()
    if pid == 0:
        try:
            os.execvp(cmd_tokens[0], cmd_tokens)
        except Exception, e:
            print(e)
    elif pid > 0:
        while True:
            wpid, status = os.waitpid(pid, 0)

            if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                break

    return SHELL_STATUS_RUN


def shell_loop():

    status = SHELL_STATUS_RUN

    while status:
        line = raw_input("> ")
        if line != "":
            cmd_tokens = tokenize(line)
            status = execute(cmd_tokens)


def main():
    shell_loop()

if __name__ == "__main__":
    main()
