#!/usr/bin/env bash

cd "$(cd `dirname $0`;pwd)"

pytest tests
