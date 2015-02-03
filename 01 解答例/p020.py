# -*- coding: utf-8 -*-
"""
Project Euler Problem 20            ○
n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.

例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.

では, 100! の各桁の数字の和を求めよ.
"""

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
a=str(factorial(100))
b=0
for i in range(0,len(a)):
    b+=int(a[i])
print b    
