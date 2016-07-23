#!/usr/bin/env python

from unittest import TestCase, main
from .. import parser


class ParserTest(TestCase):

    def test_tokens2piped_cmd(self):
        cmd = "cat /etc/hosts | grep 127"
        tokens = parser.tokenize(cmd)
        piped_cmds = parser.tokens2piped_cmd(tokens)
        self.assertEqual([['cat', '/etc/hosts'], ['grep', '127']],
                         piped_cmds)


if __name__ == "__main__":
    main()
