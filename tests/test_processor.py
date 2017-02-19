#!/usr/bin/env python

from os import path
from pysh import interpreter
from pysh.ShellProcessor import ShellProcessor, to_list

script_dir = path.dirname(path.realpath(__file__))


def exec_helper(raw_cmd):
    tokens = interpreter.tokenize(raw_cmd)
    piped_cmds = interpreter.analyze(tokens)
    return ShellProcessor(piped_cmds, to_list).run()


def test_run():
    assert ["aaa"] == exec_helper("cat %s | grep aaa" % path.join(script_dir, "cat.in"))
    assert "pysh" in exec_helper("pwd")[0]
