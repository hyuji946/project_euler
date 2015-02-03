# -*- coding: utf-8 -*-
"""
Project Euler Problem 23     
完全数とは, その数の真の約数の和がそれ自身と一致する数のことである.
 たとえば, 28の真の約数の和は, 1 + 2 + 4 + 7 + 14 = 28 であるので,
 28は完全数である.
真の約数の和がその数よりも少ないものを不足数といい, 
真の約数の和がその数よりも大きいものを過剰数と呼ぶ.

12は, 1 + 2 + 3 + 4 + 6 = 16 となるので, 
最小の過剰数である. よって2つの過剰数の和で書ける最少の数は24である.
 数学的な解析により, 28123より大きい任意の整数は2つの過剰数の和で
 書けることが知られている.
 2つの過剰数の和で表せない最大の数がこの上限よりも小さいことは
 分かっているのだが, この上限を減らすことが出来ていない.

2つの過剰数の和で書き表せない正の整数の総和を求めよ.
"""
import time
start = time.time()

from sympy import divisors
def d(n):
    return sum(divisors(n))-n

n=28123
#n=200
mylist={}
for i in range(n):
    if d(i)>i:
        mylist[i]=i
print mylist    
a=[0]*n
for j in mylist:
    for i in mylist:
        b=mylist[i]+mylist[j]
        if b>=n:
            break
        a[b]=b
ans=0
for i in range(n):
    if  a[i]==0:
        ans+= i
print ans
#30.7650001049 4179871
print time.time() - start   
