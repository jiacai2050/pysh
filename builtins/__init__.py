#!/usr/bin/env python

from .exit import exit
from .cd import cd


builtins = {
    "exit": exit,
    "cd": cd
}

__all__ = ["builtins"]
