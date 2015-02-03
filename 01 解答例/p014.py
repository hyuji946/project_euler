# -*- coding: utf-8 -*-
"""
Project Euler Problem 14            ○
正の整数に以下の式で繰り返し生成する数列を定義する.

n → n/2 (n が偶数)

n → 3n + 1 (n が奇数)

13からはじめるとこの数列は以下のようになる.

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
13から1まで10個の項になる. この数列はどのような数字からはじめても
最終的には 1 になると考えられているが, まだそのことは証明されていない(コラッツ問題)

さて, 100万未満の数字の中でどの数字からはじめれば最長の数列を生成するか.

注意: 数列の途中で100万以上になってもよい

"""
import time
start = time.time()

def f(x):
	if x%2==0:
		return x//2
	return 3*x+1
#b=100*10000	
b=100*10000
maxx=0
maxn=0
a={13:10}
for n in xrange(13,b):
    m=n
    i=1
    print n,maxx
    if m in a:
        i=a[m]
    else:
        while 1:
            m=f(m)
            if m in a:
                i=a[m]+i
                a[n]=i
                break
            if m==1:
                a[n]=i
                break
            i+=1
    if maxx<i:
        maxx=i
        maxn=n
print maxn,maxx

#76.6159999371 p014.py
#109.759000063 p014b.py
print time.time() - start   
