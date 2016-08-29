from functools import partial
from .builtins import builtins
from .util import expand_wildcard_args


class Command(object):

    @expand_wildcard_args
    def __init__(self, cmd_name, cmd_args, is_pipeline=False):
        self.cmd_name = cmd_name
        self.cmd_args = cmd_args
        self.is_pipeline = is_pipeline

        if cmd_name in builtins:
            self.cmd_runner = builtins[cmd_name]
        else:
            raise Exception("command [%s] is gone, Will you make one? PR welcomed!" % cmd_name)

    def run(self):
        if self.is_pipeline:
            return partial(self.cmd_runner, *self.cmd_args)
        else:
            return self.cmd_runner(*self.cmd_args)

    def __repr__(self):
        return ("cmd_name = %(cmd_name)s, cmd_args = %(cmd_args)s,"
                "is_pipeline = %(is_pipeline)s") % {
            "cmd_name": self.cmd_name,
            "cmd_args": self.cmd_args,
            "is_pipeline": self.is_pipeline
        }
