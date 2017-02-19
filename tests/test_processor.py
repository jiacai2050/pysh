#!/usr/bin/env python

from pysh import interpreter


def test_tokens2cmds():
    cmd = "cat /etc/hosts | grep 127"
    tokens = interpreter.tokenize(cmd)
    piped_cmds = interpreter.analyze(tokens)
    assert "cat" == piped_cmds[0].cmd_name
    assert ["/etc/hosts"] == piped_cmds[0].cmd_args
    assert "grep" == piped_cmds[1].cmd_name
    assert ["127"] == piped_cmds[1].cmd_args
