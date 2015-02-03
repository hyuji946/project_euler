# -*- coding: utf-8 -*-
"""
Project Euler Problem 15        ○
2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある.
では, 20×20 のマス目ではいくつのルートがあるか.

順列なので
2x2 右右下下　4C2 4!/((4-2)!2!)
n*m n右　m下 (n+m)Cn   (n+m)! / (n-m)! / (m)!

　
"""
def fact(n):
    if n<=0: return 1
    return fact(n-1)*n
     
def comb(n, m): return fact(n)//fact(n-m)//fact(m)
 
def f(a, b): return comb(a+b, a)
 
print f(20, 20)