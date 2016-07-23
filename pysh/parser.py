#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import shlex
from functools import partial
from .builtins import builtins
from .ShellProcessor import ShellProcessor


def tokenize(line):
    return [x.strip() for x in shlex.split(line)]


def tokens2piped_cmd(cmd_tokens):
    pipeline_sep = r"|"
    piped_cmds = []
    c = []
    for token in cmd_tokens:
        if pipeline_sep == token:
            piped_cmds.append(c)
            c = []
        else:
            c.append(token)
    else:
        piped_cmds.append(c)

    return piped_cmds


def analyze(cmd_tokens):
    if cmd_tokens[0] in builtins:
        func = builtins[cmd_tokens[0]]
        partial_args = cmd_tokens[1:]
        return func, partial_args
    else:
        print("command [%s] is gone, Will you make one? PR welcomed!" % cmd_tokens[0])


def assemble(piped_cmds):
    func, partial_args = analyze(piped_cmds[0])
    sp = ShellProcessor(func(*partial_args))

    for cmd in piped_cmds[1:]:
        func, partial_args = analyze(cmd)
        sp.add_command(partial(func, *partial_args))

    return sp
