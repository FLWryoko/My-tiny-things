from typing import cast

print('range:')
stitr = input()

itr = int(stitr)

fac =1
facc =1

print('x ,y')
for count in range(itr):
   fac = fac * facc
   print(str(count+1)+ ','+str(fac))
   facc = facc + 1
   count = count + 1


