#!/usr/bin/env python

import shlex
from functools import partial
from .builtins import builtins


class ShellProcessor(object):
    def __init__(self, source):
        self._source = source
        self._workers = []

    def add_worker(self, worker):
        self._workers.append(worker)

    def assemble(self):
        # this is the pattern for creating a generator
        # pipeline, we start with a generator then wrap
        # each consecutive generator with the pipeline itself
        # https://brett.is/writing/about/generator-pipelines-in-python/
        pipeline = self._source
        for worker in self._workers:
            pipeline = worker(pipeline)

        return pipeline


def tokenize(line):
    return map(lambda x: x.strip(), shlex.split(line))


def analyze(cmd_tokens):
    if cmd_tokens[0] in builtins:
        func = builtins[cmd_tokens[0]]
        partial_args = cmd_tokens[1:]
        return func, partial_args
    else:
        print("command [%s] is gone, Will you make one? PR welcomed!" % cmd_tokens[0])


def assemble(cmds):

    func, partial_args = analyze(tokenize(cmds[0]))
    sp = ShellProcessor(func(*partial_args))

    for cmd in cmds[1:]:
        func, partial_args = analyze(tokenize(cmd))
        sp.add_worker(partial(func, *partial_args))

    return sp.assemble


def shell_loop():

    while True:
        line = raw_input("> ")
        if line != "":
            piped_cmd_func = assemble(line.split("|"))
            for stdout in piped_cmd_func():
                print(stdout)


def main():
    shell_loop()

if __name__ == "__main__":
    main()
