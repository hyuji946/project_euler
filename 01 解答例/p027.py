# -*- coding: utf-8 -*-
"""
Project Euler Problem 27
オイラーは以下の二次式を考案している:

n**2 + n + 41.
この式は, n を0から39までの連続する整数としたときに40個の素数を生成する.
 しかし, n = 40 のとき 40**2 + 40 + 41 = 40(40 + 1) + 41 
 となり41で割り切れる. また, n = 41 のときは 41**2 + 41 + 41 
 であり明らかに41で割り切れる.

計算機を用いて, 二次式 n**2 - 79n + 1601 という式が発見できた.
 これは n = 0 から 79 の連続する整数で80個の素数を生成する.
 係数の積は, -79 × 1601 で -126479である.

さて, |a| < 1000, |b| < 1000 として以下の二次式を考える 
(ここで |a| は絶対値): 例えば |11| = 11 |-4| = 4である.

n**2 + an + b
n = 0 から始めて連続する整数で素数を生成したときに
最長の長さとなる上の二次式の, 係数 a, b の積を答えよ.
"""
from sympy import isprime
def f(a,b,n):
    return n**2+a*n+b
def check(a,b):
    n=0    
    while True:
        if isprime(f(a,b,n)):
            n+=1
        else:
            return n
#a=1;b=41
#print check(a,b)
#a=-79;b=1601
#print check(a,b)
ans=0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        c=check(a,b)
        if c>ans:
            ans=c
            ab=[a,b]
            print ans,ab
print "ans=",ab,product(ab)
            