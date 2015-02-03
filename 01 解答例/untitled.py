from sympy import factorial
from itertools import product
d='0123456789'
def cal(a):
    sa=str(a)
    s=0
    for i in range(0,len(sa)):
        s+=factorial(int(sa[i]))
    return s
"""
for i in range(10,factorial(9)*7 ):
    if cal(i)==i:
        print i
"""

for i in product("0123456789",repeat=5):
    if i[0]=="0":
        continue
    x=int(i[0]+i[1]+i[3]+i[4]+i[4])
    if x>2540160:
        continue
    if cal(x)==x:
        print x