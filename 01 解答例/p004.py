# -*- coding: utf-8 -*-
"""
Project Euler Problem 4             
左右どちらから読んでも同じ値になる数を回文数という. 
2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
では, 3桁の数の積で表される回文数の最大値を求めよ.
"""
def kai(x):
	a=str(x)
	if a==a[::-1]:
		return True
	return False

ans=0
for j in range(100,1000):
	for i in range(100,1000):
		a=i*j
		if kai(a):
			print i,j
			if ans<a:
				ans=a
print ans
