# -*- coding: utf-8 -*-
"""
Project Euler Problem 17        ○
1 から 5 までの数字を英単語で書けば one, two, three, four, five であり,
 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.

では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.
,
注: 空白文字やハイフンを数えないこと. 例えば, 342 (three hundred and forty-two) は
 23 文字, 115 (one hundred and fifteen) は20文字と数える.
 なお, "and" を使用するのは英国の慣習.
1-10



"""
snum1=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
snum2=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
snum3=["handred"]

a=snum1
for n in range(8):
    b=[(snum2[n]+"")]*9
    for i in range(len(b)):
        b[i]=b[i]+a[i]
    b=[snum2[n]]+b
    a=a+b
d=[]
for j in range(9):
    c=[snum1[j] + "hundredand"]*99        
    for i in range(99):
        c[i]=c[i]+a[i]
    c=[snum1[j]+"handred"]+c
    d=d+c
alls=a+d+["onethousand"]
print len(alls)
cnum=0
for i in range(len(alls)):
    cnum+=len(alls[i].strip(" "))
print cnum