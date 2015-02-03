# -*- coding: utf-8 -*-
"""
Project Euler Problem 10             ○
10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.
200万以下の全ての素数の和を求めよ.
"""
from  sympy import isprime
ans=0
for i in range(2,2*10**6):
    if isprime(i)==True:
        ans+=i
print ans
