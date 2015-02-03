# -*- coding: utf-8 -*-
"""
Project Euler Problem 6             ○
最初の10個の自然数について, その二乗の和は,
12 + 22 + ... + 102 = 385
最初の10個の自然数について, その和の二乗は,
(1 + 2 + ... + 10)2 = 3025
これらの数の差は 3025 - 385 = 2640 となる.
同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
"""
ans=0
ans2=0
for i in range (1,101):
    ans+=i*i
    ans2+=i
print ans
print ans2*ans2
print ans2*ans2-ans    