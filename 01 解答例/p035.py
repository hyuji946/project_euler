# -*- coding: utf-8 -*-
"""
===================================
Project Euler Problem 35
===================================
197は巡回素数と呼ばれる. 桁を回転させたときに得られる数 197, 971, 719 が全て素数だからである.
100未満には巡回素数が13個ある: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, および97である.
100万未満の巡回素数はいくつあるか?

===================================
"""

from sympy import isprime
def fc(sa):    #１回桁をずらす
    a=sa[1::]+sa[0]
    return a
def isjp(sa):
    for i in range(len(sa)):
        if not isprime(int(sa)):
            return False
        sa=fc(sa)
    return True
ans=0
for i in range(1,100*10000):
    if isjp(str(i)):
        ans+=1
        print ans,i
        
        
    
