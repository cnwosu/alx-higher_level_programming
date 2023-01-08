#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    words = "argument"
    period = '.'

    if argc != 1:
        words += 's'
    if argc != 0:
        period = ':'
    print("{} {}{}".format(argc, words, period))
    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
