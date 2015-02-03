# -*- coding: utf-8 -*-
"""
Project Euler Problem 9             ○
ピタゴラス数(ピタゴラスの定理を満たす自然数)とは
 a < b < c で以下の式を満たす数の組である.
a^2 + b^2 = c^2
例えば, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 である.
a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい.
"""

for c in xrange(3,1000):
    for b in xrange(2,1000):
        if c+b>1000:
            break
        if c<b:
            break
        for a in xrange(1,1000):
            if b<a:
                break
            if a+b+c>1000:
                break
            if a<b<c:
                if c+b+a==1000:
                    if c*c==b*b+a*a:
                        print "a=",a,"b=",b,"c=",c
                        print "a+b+c=",a+b+c
                        print "a*b*c=",a*b*c
                
