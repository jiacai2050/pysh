#!/usr/bin/env bash

cd "$(cd `dirname $0`;pwd)"

python -m unittest discover
