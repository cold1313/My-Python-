6 nomer:

from itertools import *
alphabet = "0123456789"
s1 = "02468"
s2 = "13579"
arr = product(alphabet , repeat=4)
count = 0
for elem in arr:
    Flag = True
    if elem[0] != "0":
        for j in range(3):
            if (elem[j] in s1 and elem[j+1] in s1) or (elem[j] in s2 and elem[j+1] in s2):
                Flag = False
                break
        for j in range(4):
            if elem.count(elem[j]) > 1:
                Flag = False
                break
        if Flag:
            count += 1
print(count)




from itertools import *
arr = product("БРОНХИ" , repeat=4)
count = 0
for elem in arr:
    if elem.count("Х") == 1:
        count += 1
print(count) 


14 nomer: 
def f(x):
    if x == 0:
        return 0
    if x > 0 and x % 3 == 2:
        return f(x-1) + 1
    if x > 0 and x % 3 < 2:
        return f((x- x%3) / 3)
    
for x in range(1000):
    if f(x) == 6:
        print(x)
        break

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


def f(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if x > 2: 
        return f(x-2) * x
print(f(7))

f = open("text17" , "r")
arr = list(f.readlines())
numofpar = 0
maxpara = -10**9
for i in range(len(arr)):
    for j in range(i + 1 , len(arr)):
        if (int(arr[i]) - int(arr[j])) % 80 == 0:
            numofpar += 1
            if int(arr[i]) - int(arr[j]) > maxpara:
                maxpara = int(arr[i]) - int(arr[j])
print(numofpar , maxpara)


f = open("text17" , "r")
arr = list(f.readlines())
count = 0
min = 10**9
maxpar = -10**9
for i in range(len(arr)):
    if int(arr[i]) < min and abs(int(arr[i])) % 10 == 6:
        min = int(arr[i])
for i in range(len(arr)-1):
    if ((abs(int(arr[i])) % 10 == 6 and abs(int(arr[i+1])) % 10 != 6 or abs(int(arr[i])) % 10 != 6 and abs(int(arr[i+1])) % 10 == 6) 
        and int(arr[i])**2 + int(arr[i+1])**2 < min ** 2):
        count += 1
        if (int(arr[i])**2 + int(arr[i+1])**2) > maxpar:
            maxpar = int(arr[i])**2 + int(arr[i+1])**2

print(count , maxpar)
        
    
f = open("text17" , "r")
arr = list(f.readlines())
maxnum = -10**9
count = 0
maxpar = -10**9
for i in range(len(arr)):
    if int(arr[i]) > maxnum and arr[i][-2] == "3":
        maxnum = int(arr[i])
print(maxnum)
for i in range(len(arr) -1):
    if arr[i][-2] == "3" and arr[i+1][-2] != "3" or arr[i][-2] != "3" and arr[i+1][-2] == "3":
        if (int(arr[i]) ** 2 + int(arr[i+1]) ** 2) >= maxnum **2 :
            count += 1
            if (int(arr[i])**2 + int(arr[i+1])**2) > maxpar:
                maxpar = int(arr[i])**2 + int(arr[i+1])**2
print(count , maxpar)

    

