ans = 0
arr = [8 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]
arr2 = [9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]
for i in range(len(arr)):
    a = 1
    for j in range(len(arr) - i):
        a *= arr[j]
    ans += a

for i in range(len(arr2)):
    a = 1
    for j in range(len(arr2) - i):
        a *= arr2[j]
    ans += a

print(ans + 2) #если число 0 или 5



from itertools import *
count = 0
arr = product('АОУ', repeat=5)
for x in arr:
    count += 1
    if count == 125:
        print(x)
        break



from itertools import product

ans = 0
arr = product('РЕГИНА', repeat=5)
for elem in arr:
    if elem.count('Р') == 1 and elem.count('Г') == 1 and elem.count('Н') <= 1:
        ans += 1
print(ans)
