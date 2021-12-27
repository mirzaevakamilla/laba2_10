#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sred_geom(*args):
    if args:
        summa = 0
        for arg in args:
            summa = summa + arg
        n = len(args)
        return summa // n
    else:
        return None


if __name__ == "__main__":
    print(sred_geom(21, 4, 6, 8))
