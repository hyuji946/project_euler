# -*- coding: utf-8 -*-
"""
Project Euler Problem 1             
10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは
 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.
同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.
"""
def f35(x):
    if x%3==0 or x%5==0:
        return  True
    else:
        return False
ans=0
for i in range(1,1000):
    if f35(i):
        ans+=i
        print i
print "ans=", ans

    