from functools import partial
from glob import glob
from .builtins import builtins


def expand_wildcard_args(func):
    def wrapper(this, cmd_name, cmd_args, is_pipeline=False):
        if cmd_args is not None and len(cmd_args) > 0:
            expanded_args = []
            for arg in cmd_args:
                matched_items = glob(arg)
                if len(matched_items) == 0:
                    expanded_args.append(arg)
                else:
                    expanded_args += matched_items
            cmd_args = expanded_args

        return func(this, cmd_name, cmd_args, is_pipeline)

    return wrapper


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
