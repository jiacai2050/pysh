#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)


class ShellProcessor(object):
    def __init__(self, source):
        self._source = source
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def run(self):

        # this is the pattern for creating a generator
        # pipeline, we start with a generator then wrap
        # each consecutive generator with the pipeline itself
        # https://brett.is/writing/about/generator-pipelines-in-python/
        pipeline = self._source
        for command in self._commands:
            pipeline = command(pipeline)

        for val in pipeline:
            if val is not None:
                print(val)
