#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)


def console(pipeline):
    for val in pipeline:
        if val is not None:
            print(val)


def to_list(pipeline):
    return [o for o in pipeline]


class ShellProcessor(object):
    def __init__(self, cmds, stdout=console):
        self._source = cmds[0]
        self._commands = cmds[1:]
        self.stdout = stdout

    def run(self):

        # this is the pattern for creating a generator
        # pipeline, we start with a generator then wrap
        # each consecutive generator with the pipeline itself
        # https://brett.is/writing/about/generator-pipelines-in-python/
        pipeline = self._source.run()
        for command in self._commands:
            pipeline = command.run()(pipeline)

        return self.stdout(pipeline)
