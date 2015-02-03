# -*- coding: utf-8 -*-
"""
===================================
Project Euler Problem 37
===================================
3797は面白い性質を持っている. まずそれ自身が素数であり,
 左から右に桁を除いたときに全て素数になっている 
 (3797, 797, 97, 7).
 同様に右から左に桁を除いたときも全て素数である 
 (3797, 379, 37, 3).
右から切り詰めても左から切り詰めても素数
になるような素数は11個しかない. 総和を求めよ.
注: 2, 3, 5, 7を切り詰め可能な素数とは考えない.
===================================
from sympy isprime
"""
def lcheck(n):
    a=str(n)
    for i in range(len(a)):
        if not isprime(int(a)):
            return False
        a=a[1::]
    return True
def rcheck(n):
    a=str(n)
    for i in range(len(a)):
        if not isprime(int(a)):
            return False
        a=a[:len(a)-1]
    return True
flag=0
i=10
ans=0
while True:
    if lcheck(i) and rcheck(i):
        flag+=1
        ans+=i
        print flag,i
        if flag==11:
            break
    i+=1
print "ans = ",ans

        