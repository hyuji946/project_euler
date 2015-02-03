# -*- coding: utf-8 -*-
"""
Project Euler Problem 16            ○
2^15 = 32768 であり, これの数字和 ( 各桁の和 ) は 3 + 2 + 7 + 6 + 8 = 26 となる.

同様にして, 2^1000 の数字和を求めよ.
"""

a=2**1000
b=str(a)
ans=0
for i in range(0,len(b)):
    ans+=int(b[i])
print ans