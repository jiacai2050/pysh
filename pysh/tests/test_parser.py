#!/usr/bin/env python

from unittest import TestCase, main
from os import path, chdir
from .. import parser


class ParserTest(TestCase):

    def test_tokens2piped_cmd(self):
        cmd = "cat /etc/hosts | grep 127"
        tokens = parser.tokenize(cmd)
        piped_cmds = parser.tokens2piped_cmd(tokens)
        self.assertEqual([['cat', '/etc/hosts'], ['grep', '127']],
                         piped_cmds)

    def test_analyze(self):
        script_dir = path.dirname(path.realpath(__file__))
        chdir(script_dir)
        cmd = "ls __i*t__.p?"
        cmd_name, cmd_args = parser.analyze(parser.tokenize(cmd))
        self.assertEqual(["__init__.py"], cmd_args)


if __name__ == "__main__":
    main()
