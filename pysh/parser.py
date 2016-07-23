#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import shlex
from functools import partial
from .builtins import builtins
from .ShellProcessor import ShellProcessor
from .util import expand_wildcard_args, stderr_print


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


@expand_wildcard_args
def analyze(cmd_tokens):
    if cmd_tokens[0] in builtins:
        cmd_name = builtins[cmd_tokens[0]]
        cmd_args = cmd_tokens[1:]
        return cmd_name, cmd_args
    else:
        stderr_print("command [%s] is gone, Will you make one? PR welcomed!" % cmd_tokens[0])


def assemble(piped_cmds):
    cmd_name, cmd_args = analyze(piped_cmds[0])
    sp = ShellProcessor(cmd_name(*cmd_args))

    for cmd in piped_cmds[1:]:
        cmd_name, partial_args = analyze(cmd)
        sp.add_command(partial(cmd_name, *partial_args))

    return sp
