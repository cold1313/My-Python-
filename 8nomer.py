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


from itertools import *
count = 0
arr = product("АВХ" , repeat=6)
for x in arr:
    if x.count("Х") == 1:
        count += 1
print(count)


from itertools import *
count = 0
arr = product("КОНФЕТА" , repeat=5)
for x in arr:
    if x.count("Е") == 2 and x[1] != "Ф":
        count += 1
print(count)


from itertools import *
c1 = '1357'
c2 = '2468'
count = 0
for i in product(c1,c2,c1,c2,c1,c2,c1,c2,c1,c2,c1):
    s = ''.join(i)
    flag = 1
    for i in range(10):
        if s.count (str(i)) > 4:
            flag = 0
            break
    if flag:
        count += 1        
print(count * 2)


from itertools import product   
cnt = 0
num = 0
arr = product('АГИЛМОРТ', repeat=5) #если написано в алфавитном порядке, то букввы в слове надо писать по алфавиту! 
for elem in arr:
    num += 1
    if elem[0] != "Г" and elem.count("И") >= 2 and num % 2 != 0:
        cnt += 1
print(cnt)

from itertools import product
count = 0
num = 0
arr = product("ЕИМНРТ" , repeat=10)
for elem in arr:
    num += 1
    if num % 3 == 0 and (elem[0] == "Е" or elem[0] == "И") and elem.count("Т") == 1:
        count += 1
print(count)


from itertools import *
count = 0
arr = product("МЕТРО" , repeat=4)
for x in arr:
    if (x[0] == "Е" or x[0] == "О") and (x[3] == "М" or x[3] == "Т" or x[3] == "Р"):
        count += 1
print(count)

from itertools import *
count = 0
arr = product("012345678" , repeat=5)
for x in arr:
    if x.count("5") == 1 and x[0] != "0":
