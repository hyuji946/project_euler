# -*- coding: utf-8 -*-
"""
Project Euler Problem 19            ○
次の情報が与えられている.

1900年1月1日は月曜日である.
9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
2月は28日まであるが, うるう年のときは29日である.
うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.
20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
"""
from datetime import date

summ=0
tmp=0
for j in range(1901,2001):
    for i in range(1,13):
        if date(j,i,1).weekday()==6:
            tmp+=1
    summ+=tmp
    print j,tmp,summ
    tmp=0



