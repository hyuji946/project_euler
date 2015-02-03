# -*- coding: utf-8 -*-
"""
Project Euler Problem 26
単位分数とは分子が1の分数である. 分母が2から10の単位分数を10進数で表記すると
次のようになる.

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

0.1(6)は 0.166666... という数字であり, 1桁の循環節を持つ. 
1/7 の循環節は6桁ある.
d < 1000 なる 1/d の中で小数部の循環節が最も長くなるような d を求めよ.
"""
def cycle(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return 0
    count = 1
    while 10**count % n != 1:
        count += 1
    return count
ans=0
ans2=0
for i in range(1,1000):
    a= cycle(i)
    if ans < a:
        ans=a
        ans2=i
        print ans2,ans