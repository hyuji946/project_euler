# -*- coding: utf-8 -*-
"""
Project Euler Problem 21
            
d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき,
 a と b は友愛数(親和数)であるという.

例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので
 d(220) = 284 である.
また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

それでは10000未満の友愛数の和を求めよ.

"""
import time
start = time.time()


def yak(x):
    ans=[]

    for i in xrange(1,x):
        if x%i == 0:
            ans.append(i)
    return ans
    
def d(n):
    return sum(yak(n))
def ai(n):
    a=d(n)
    b=d(a)
#a==nの時は完全数　6,28,496
    if b==n and not a==n:
        return True
    else:
        return False
ans=0
for i in xrange(2,10000):
    if ai(i):
        ans+=i
        print i
print ans

#146.905999899
print time.time() - start   