# -*- coding: utf-8 -*-
"""
===================================
Project Euler Problem 39
===================================
辺の長さが {a,b,c} と整数の3つ組である直角三角形を考え,
 その周囲の長さを p とする. p = 120のときには3つの解が存在する:

{20,48,52}, {24,45,51}, {30,40,50}

p ≤ 1000 のとき解の数が最大になる p はいくつか?

===================================
"""
#a⊥bとする
#a+b+c=p a,b,c,pは正の整数
#c**2=a**2+b**2
#c<a+b b<a+c a<b+c
ans=0
ansa=[]
for a in range(1,1000):
    for b in range(a,1000):
        c=(a**2+b**2)**0.5
        if int(c)==c:
            p=a+b+int(c)
            if p<=1000:
                if ans<p:
                    ans=p
                ansa.append([p,a,b,int(c)])
ansa=sorted(ansa)
num=0
ans=0
ans2=0
for i in range(len(ansa)-1):
    if ansa[i][0]==ansa[i+1][0]:
        num+=1
    else:
        if ans<num+1:
            ans=num+1
            ans2=ansa[i][0]
        print ansa[i],num+1
        num=0
print "ans = ",ans,u"個 ","p = ",ans2
                
