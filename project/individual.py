#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def s_mod(*args):
    if args:
        elms = [abs(i) for i in args]
        min_elem = min(elms)
        idx = elms.index(min_elem)
        summa = sum(elms[idx + 1:])
        return summa
    else:
        return None


if __name__ == "__main__":
    print(s_mod(8, 10, -10, 7, 5, 10))
