6 nomer:

from itertools import *
alphabet = "0123456789"
s1 = "02468"
s2 = "13579"
arr = product(alphabet , repeat=4)
ans = []
count = 0
for i in arr:
    ans = ''.join(i)
Flag = True
for i in range(len(ans) - 1):
    if (ans[i] in s1 and ans[i+1] in s1) or (ans[i] in s2 and ans[i+1] in s2) and ans[0] == 0:
        Flag = False
    if Flag == True:
        count += 1
print(count)


from itertools import *
arr = product("БРОНХИ" , repeat=4)
count = 0
for elem in arr:
    if elem.count("Х") == 1:
        count += 1
print(count) 


from itertools import *
arr = product("ABCX" , repeat=5)
count = 0
for elem in arr:
    if (elem.count("X") == 1 and elem[4] == "X") or (elem.count("X") == 0):
        count += 1
print(count)

def f(x):
    if x == 1:
        return 1
    if x == 2: 
        return 3
    if x > 2:
        return f(x-1) * x + f(x-2) * (x-1)
print(f(5))