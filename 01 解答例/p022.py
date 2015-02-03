# -*- coding: utf-8 -*-
"""
Project Euler Problem 2 2       
5000個以上の名前が書かれている46Kのテキストファイル
names.txt を用いる. まずアルファベット順にソートせよ.
のち, 各名前についてアルファベットに値を割り振り,
 リスト中の出現順の数と掛け合わせることで, 名前のスコアを計算する.

たとえば, リストがアルファベット順にソートされているとすると,
 COLINはリストの938番目にある. またCOLINは
 3 + 15 + 12 + 9 + 14 = 53 という値を持つ. 
 よってCOLINは 938 × 53 = 49714 というスコアを持つ.

ファイル中の全名前のスコアの合計を求めよ.

"""
from itertools import islice
f=open("names.txt")
data=f.read()
names=data.split(",")
names2=[]
for i in names:
    names2.append(i.strip('"'))
names=sorted(names2)
#a=names.index('COLIN')+1
dictionary = dict((c, n) for (n, c) in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1))
sum1=0
for j in names:
    a=names.index(j)+1
    sum2=0
    for i in islice(j,len(j)):
        sum2+=dictionary[i]
    sum1+=a*sum2
print sum1
    
