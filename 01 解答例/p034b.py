# -*- coding: utf-8 -*-
"""
===================================
Project Euler Problem 34
===================================
145は面白い数である. 1! + 4! + 5! = 1 + 24 + 120 = 145となる.

各桁の数の階乗の和が自分自身と一致するような数の和を求めよ.

注: 1! = 1 と 2! = 2 は総和に含めてはならない.
===================================
8桁になるとすべて９でも二乗の和は７桁にしかならない
７桁まで９！＊７＝2540160　以下の数字を計算
２桁　４まで　３桁６まで　４桁７まで　５桁８まで
"""
from sympy import factorial
from itertools import product
d='0123456789'
def cal(sa):
#    sa=str(a)
    s=0
    for i in range(0,len(sa)):
        s+=factorial(int(sa[i]))
    return s
"""
for i in range(10,factorial(9)*7 ):
    if cal(i)==i:
        print i
"""
for i in product("01234",repeat=2):
    if i[0]=="0":
        continue
    x=(i[0]+i[1])
    if cal(sorted(x))==int(x):
        print x
for i in product("0123456",repeat=3):
    if i[0]=="0":
        continue
    x=(i[0]+i[1]+i[2])
    if cal(sorted(x))==int(x):
        print x
for i in product("01234567",repeat=4):
    if i[0]=="0":
        continue
    x=(i[0]+i[1]+i[2]+i[3])
    if cal(sorted(x))==int(x):
        print x
for i in product("012345678",repeat=5):
    if i[0]=="0":
        continue
    x=(i[0]+i[1]+i[2]+i[3]+i[4])
    if cal(sorted(x))==int(x):
        print x
for i in product("0123456789",repeat=6):
    if i[0]=="0":
        continue
    x=(i[0]+i[1]+i[2]+i[3]+i[4]+i[5])
    if cal(sorted(x))==int(x):
        print x
for i in product("0123456789",repeat=7):
    if i[0]=="0":
        continue
    x=(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6])
    if x>2540160:
        continue
    if cal(sorted(x))==int(x):
        print x

        