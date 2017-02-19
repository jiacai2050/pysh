#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import shlex
from .Command import Command


def tokenize(line):
    return [x.strip() for x in shlex.split(line)]


def analyze(cmd_tokens):
    pipeline_sep = r"|"
    cmds = []
    current_cmd = []

    is_pipeline = False
    for token in cmd_tokens:
        if pipeline_sep == token:
            cmds.append(Command(current_cmd[0], current_cmd[1:], is_pipeline))
            is_pipeline = True
            current_cmd = []
        else:
            current_cmd.append(token)
    else:
        cmds.append(Command(current_cmd[0], current_cmd[1:], is_pipeline))
    return cmds
