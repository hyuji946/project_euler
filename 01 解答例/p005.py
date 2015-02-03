# -*- coding: utf-8 -*-
"""
Project Euler Problem 5             
2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり,
 そのような数字の中では最小の値である.
では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.
"""
from sympy import factorint

def mycheck(n):
    for i in range(2,21):
        if not n%i==0:
            return 0
    return 1

ans = 0
mylist=[0]*21
for i in range(2,21):
    li=factorint(i).keys()
    lv=factorint(i).values()
    k=0
    print i,li,lv
    for j in li:
        if mylist[j]<lv[k]:
            mylist[j]=lv[k]
        k+=1
print mylist
xx=1
for i in range(2,21):
    if not mylist[i]==0:
        xx*=i**mylist[i]
print "ans = ",xx
if mycheck(xx):
    print "ok"
else:
    print "error"    
    
    
            
    
