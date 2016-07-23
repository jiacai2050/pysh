#!/usr/bin/env bash

## start wrapper

cd "$(cd `dirname $0`;pwd)"

## In unix-like OS, rlwrap used for command line edit and history
## In Windows, line edit is supported out of box but history is impossible for now.
rlwrap python -m pysh.shell
