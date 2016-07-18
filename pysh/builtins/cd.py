#!/usr/bin/env python

from ..constants import SHELL_STATUS_RUN
import os


def cd(args):
    os.chdir(args[0])
    return SHELL_STATUS_RUN
