# -*- coding: utf-8 -*-
"""
===================================
Project Euler Problem 32 x
===================================
すべての桁に 1 から n が一度だけ使われている数をn桁の数がパンデジタル 
(pandigital) であるということにしよう: 例えば5桁の数 15234 は1から5のパンデジタルである.

7254 は面白い性質を持っている. 39 × 186 = 7254 と書け, 掛けられる数, 掛ける数, 積が1から9のパンデジタルとなる.

掛けられる数/掛ける数/積が1から9のパンデジタルとなるような積の総和を求めよ.

HINT: いくつかの積は, 1通り以上の掛けられる数/掛ける数/積の組み合わせを持つが1回だけ数え上げよ.
===================================
divisor_count 約数の数　divisor　約数リスト　primefactors　素因数リスト　factorint　素因数dict
prime(n) n番目の素数　isprime 素数判定
product('ABC',repeat=2) -> AA AB AC BA BB BC CA CB CC	直積 （ＡＡ、ＢＡがある）
permutations('ABC',2) -> AB AC BA BC CA CB 				順列　Ｐ　（ＡＡがない）
combinations('ABC',2) -> AB AC BC 						組み合わせ　Ｃ　（ＡＡ、ＢＡがない）
combinations_with_replacement('ABC',2) -> AA AB AC BB BC CC	繰り返し有りの組み合わせ　（ＡＡがありＢＡはない）
---------------------
from datetime import date
from itertools import combinations, permutations
from itertools import islice,product,combinations_with_replacement
from math import sqrt, log, log10, ceil
from numpy import  arange
from sympy import divisor_count, divisors, factorint, isprime, prime, primefactors
import operator, os, string, time
"""
#1桁＊４桁＝４桁
#2桁＊3桁＝4桁

from itertools import permutations
a='123456789'
s=0
for i in permutations(a,9):
    ab=int(i[0])*int(i[1]+i[2]+i[3]+i[4])
    c=int(i[5]+i[6]+i[7]+i[8])
    if ab==c:
        s+=c
        print"1x4 ",c
        continue
    ab=int(i[0]+i[1])*int(i[2]+i[3]+i[4])
    c=int(i[5]+i[6]+i[7]+i[8])
    if ab==c:
        s+=c
        print"2*3 ",c
        continue
print "ans = ",s