#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import shlex
from .ShellProcessor import ShellProcessor
from .Command import Command


def tokenize(line):
    return [x.strip() for x in shlex.split(line)]


def tokens2cmds(cmd_tokens):
    pipeline_sep = r"|"
    cmds = []
    current_cmd = []
    is_pipeline = False
    for token in cmd_tokens:
        if pipeline_sep == token:
            if is_pipeline:
                cmds.append(Command(current_cmd[0], current_cmd[1:], True))
            else:
                cmds.append(Command(current_cmd[0], current_cmd[1:]))
            is_pipeline = True
            current_cmd = []
        else:
            current_cmd.append(token)
    else:
        if is_pipeline:
            cmds.append(Command(current_cmd[0], current_cmd[1:], True))
        else:
            cmds.append(Command(current_cmd[0], current_cmd[1:]))
    return cmds


def assemble(cmds):
    source_cmd = cmds[0]
    sp = ShellProcessor(source_cmd.run())

    for piped_cmd in cmds[1:]:
        sp.add_command(piped_cmd.run())

    return sp
