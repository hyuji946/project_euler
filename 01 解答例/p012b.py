# -*- coding: utf-8 -*-
"""
Ploject Euler Problem 12            ○
三角数の数列は自然数の和で表わされ, 7番目の三角数は
 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 である.
 三角数の最初の10項は:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
となる.

最初の7項について, その約数を列挙すると, 以下のとおり.

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

これから, 7番目の三角数である28は, 5個より多く約数をもつ最初の三角数であることが分かる.

では, 500個より多く約数をもつ最初の三角数はいくつか.
"""
from sympy import divisor_count
from numpy import  arange

def sankaku(n):
	return sum(arange(1,n+1))
n=7
while True :
	b = sankaku(n)
	a = divisor_count(b)
	print a,b
	if a>=500:
		break
	n+=1
print n,b,a    

        
