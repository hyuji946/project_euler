# -*- coding: utf-8 -*-
"""
Project Euler Problem 3             ○
13195 の素因数は 5, 7, 13, 29 である.
600851475143 の素因数のうち最大のものを求めよ.
"""
from sympy import primefactors
n=600851475143
a=primefactors(n)
print a
print max(a)





