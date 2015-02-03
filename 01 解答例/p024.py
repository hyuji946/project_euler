# -*- coding: utf-8 -*-
"""
Project Euler Problem 24       　○
順列とはモノの順番付きの並びのことである.
 たとえば, 3124は数 1, 2, 3, 4 の一つの順列である.
 すべての順列を数の大小でまたは辞書式に並べたものを辞書順と呼ぶ.
 0と1と2の順列を辞書順に並べると

012 021 102 120 201 210
になる.

0,1,2,3,4,5,6,7,8,9からなる順列を辞書式に並べたときの100万番目はいくつか?
"""
import time
start = time.time()

from itertools import permutations
from itertools import combinations
data=[0,1,2,3,4,5,6,7,8,9]
i=1
for element in permutations(data, 10):
#    print i,element
    if i==100*10000:
        break
    i+=1
print "ans=","".join([str(i) for i in element])
#0.825999975204 2783915460
print time.time() - start   
