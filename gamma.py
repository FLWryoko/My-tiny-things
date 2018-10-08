from math import factorial
from typing import cast

n=0
m=0
print('range:')
stitr = input()
itr = int(stitr)
for count in range(itr):
    if count==0:
        print('x')
        n = input() 
        m = float(n)
    gamma = m*(m-1)
    stgamma = str(gamma)
    stm = str(m)
    print('x:m'+ stm+ 'y:'+stgamma)
    m = m-0.1
    count + 1
