#!/usr/bin/env python

from __future__ import (
    print_function, absolute_import, unicode_literals
)
import requests
from ..util import stderr_print


def run(*args):
    if len(args) == 0:
        stderr_print("curl: missing one param")
        yield None
    else:
        to_fetch_urls = args
        if isinstance(to_fetch_urls, basestring):
            to_fetch_urls = [to_fetch_urls]

        for to_fetch_url in to_fetch_urls:
            r = requests.get(to_fetch_url)
            for line in r:
                yield line
