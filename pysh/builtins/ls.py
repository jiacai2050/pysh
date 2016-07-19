#!/usr/bin/env python

import os


def run(*f_or_dirs):
    if len(f_or_dirs) == 0:
        for f_or_dir in os.listdir(os.getcwd()):
            yield f_or_dir
    else:
        for f_or_dir in f_or_dirs:
            if os.path.exists(f_or_dir):
                if os.path.isfile(f_or_dir):
                    yield f_or_dir
                else:
                    for sub_f_or_dir in os.listdir(f_or_dir):
                        yield sub_f_or_dir
            else:
                print("%s doesn't exists" % f_or_dir)