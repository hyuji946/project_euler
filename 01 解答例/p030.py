# -*- coding: utf-8 -*-
"""
Project Euler Problem 30
驚くべきことに, 各桁を4乗した数の和が元の数と一致する数は3つしかない.

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
ただし, 1=1*4は含まないものとする. この数たちの和は 1634 + 8208 + 9474 = 19316 である.

各桁を5乗した数の和が元の数と一致するような数の総和を求めよ.

"""
ans=0
for i in range(1000,10000):
    s=str(i)
#    if int(s[0])**4+int(s[1])**4+int(s[2])**4+int(s[3])**4==i:
    if int(s[0])**5+int(s[1])**5+int(s[2])**5+int(s[3])**5==i:
        print i
        ans+=i
for i in range(10000,100000):
    s=str(i)
#    if int(s[0])**4+int(s[1])**4+int(s[2])**4+int(s[3])**4==i:
    if int(s[0])**5+int(s[1])**5+int(s[2])**5+int(s[3])**5+int(s[4])**5==i:
        print i
        ans+=i
for i in range(100000,1000000):
    s=str(i)
#    if int(s[0])**4+int(s[1])**4+int(s[2])**4+int(s[3])**4==i:
    if int(s[0])**5+int(s[1])**5+int(s[2])**5+int(s[3])**5+int(s[4])**5+int(s[5])**5==i:
        print i
        ans+=i
print "ans=",ans

            