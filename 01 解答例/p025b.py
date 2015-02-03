# -*- coding: utf-8 -*-
"""
Project Euler Problem 25
フィボナッチ数列は以下の漸化式で定義される:

Fn = Fn-1 + Fn-2, ただし F1 = 1, F2 = 1.
最初の12項は以下である.

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
12番目の項, F12が3桁になる最初の項である.

1000桁になる最初の項の番号を答えよ.
"""
from itertools import count, imap, takewhile, tee, izip
def first(iterable):
    """Take first element in the iterable"""
    return iterable.next()
def fibonacci():
    """Generate fibonnacci serie"""
    get_next = lambda (a, b), _: (b, a+b)
    return (b for (a, b) in ireduce(get_next, count(), (0, 1)))
def ireduce(func, iterable, init=None):
    """Like reduce() but using iterators (a.k.a scanl)"""
    # not functional
    if init is None:
        iterable = iter(iterable)
        curr = iterable.next()
    else:
        curr = init
        yield init
    for x in iterable:
        curr = func(curr, x)
        yield curr
print first(idx for (idx, x) in enumerate(fibonacci(), 1) if x >= 10**999)
