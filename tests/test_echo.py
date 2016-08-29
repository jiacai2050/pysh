#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
from pysh.builtins import echo
import os


def test_echo():
    ret = echo.run("\$abc")
    assert "\$abc" == next(ret)

    ret = echo.run("$USER ${USER}")
    env_user = os.getenv("USER", "")
    assert "%(env_user)s %(env_user)s" % {
        "env_user": env_user
    } == next(ret)
