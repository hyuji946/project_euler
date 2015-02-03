# -*- coding: utf-8 -*-
"""
===================================
Project Euler Problem 33    ○
===================================
49/98は面白い分数である.「分子と分母からそれぞれ9を取り除くと,
 49/98 = 4/8 となり, 簡単な形にすることができる」と経験の浅
 い数学者が誤って思い込んでしまうかもしれないからである. 
 (方法は正しくないが，49/98の場合にはたまたま正しい約分になってしまう．)

我々は 30/50 = 3/5 のようなタイプは自明な例だとする.

このような分数のうち, 1より小さく分子・分母がともに2桁の数に
なるような自明でないものは, 4個ある.

その4個の分数の積が約分された形で与えられたとき, 分母の値を答えよ.
===================================

"""
#ab/bc ab<bc a/c=ab/bc
#
from sympy import *
from itertools import product
z=Rational(1,1)
d='0123456789'
for i in product(d,repeat=4):
    sa=i[0]+i[1];sb=i[2]+i[3]
    ia=int(sa);ib=int(sb)
    if sa==sb or  ia>ib or ia==0 or ib==0 or i[0]=="0"or i[2]=="0":
        continue
    x=Rational(ia, ib)
    if i[0]==i[2]:
        y=Rational(int(i[1]), int(i[3]))
        if x==y:
            z*=x
            print sa,sb,x,y
    if i[0]==i[3]:
        y=Rational(int(i[1]), int(i[2]))
        if x==y:
            z*=x
            print sa,sb,x,y
    if i[1]==i[2]:
        y=Rational(int(i[0]), int(i[3]))
        if x==y:
            z*=x
            print sa,sb,x,y
    if i[1]==i[3] and i[1]<>"0":
        y=Rational(int(i[0]), int(i[2]))
        if x==y:
            z*=x
            print sa,sb,x,y
print z
