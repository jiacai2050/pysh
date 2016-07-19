#!/usr/bin/env python

import os
import re

# FIX: variables in singe quote should not expand
# http://stackoverflow.com/a/2973495/2163429
var_re = re.compile(r"(?<!\\)\${?(\w+)}?")


def run(*args):
    for var_or_literal in args:
        yield var_re.sub(lambda env_var_match: os.getenv(env_var_match.group(1), " "),
                         var_or_literal)


if __name__ == '__main__':
    for x in run(r"\$abc",
                 r"${HOME} ${JAVA_HOME} $USER",
                 r"\${HOME}",
                 r"'${HOME}'"):
        print(x)
