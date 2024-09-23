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


from itertools import *
arr = product("0123" , repeat=3)
count = 0
for i in arr:
    if i[0] != "0" and int(i[0]) + int(i[2]) > int(i[1]):
        count += 1
print(count)


from itertools import *
count = 0
arr = product("0234567" , repeat = 5)
for i in arr:
    if i[0] != "0":
        check = True
        ar = set()
        for j in range(len(i)-1):
            ar.add(i[j])
            if (int(i[j]) + int(i[j+1])) % 2 == 0:
                check = False
        ar.add(i[-1])
        if check == True and len(ar) == len(i):
            count += 1
print(count)

from itertools import *
arr = product("012345678" , repeat = 6)
ans = 0
for i in arr:
    count_odd = 0
    for j in range(len(i)):
        if int(i[j]) % 2 != 0:
            count_odd += 1
    if count_odd == 2 and i[0] != "0" and i.count('4') == 1:
        ans += 1
print(ans)

from itertools import *
arr = product("МУЖЧИНА" , repeat = 6)
count = 0
num = 1
for i in arr:
    if i[0] != "Ч" and i.count("Ж") == 1 and i.count("М") <= 1 and i.count("У") <= 1 and i.count("Ч") <= 1 and i.count("И") <= 1 and i.count("Н") <= 1 and i.count("А") <= 1: 
        if num%2 != 0:
            count += 1
        num += 1
print(count)


from itertools import *
arr = product("0123" , repeat = 3)
count = 0
for i in arr:
    if int(i[0]) + int(i[2]) > int(i[1]):
        count += 1
print(count)


40 nomer dz: 

import itertools 
alphabet = "ABCDXYZ"
s = 'XYZ'
s1 = 'ABCD'
ar = itertools.product(alphabet, repeat=4) #Размещение с повторением
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e[0] in s and e[1] in s and e[2] in s1 and e[3] in s1:
        count += 1
print(count)

from itertools import *
x = "01234567"
arr = permutations(x , 5)
ans = 0
for elem in arr:
    if elem[0] == "0":
        continue
    flag = True
    for letter in elem:
        if elem.count(letter) > 1:
            flag = False
            break
    if flag == False:
        continue
    flag = True
    for i in range(len(elem)-1):
        if (int(elem[i]) + int(elem[i + 1]))%2 == 0:
            flag = False
            break
    if flag == True:
        ans += 1
print(ans)


from itertools import *
x = "01234567"
ans = 0
arr = product(x , repeat = 5)
for elem in arr:
    if elem[0] == "0" or elem.count("1") > 0:
        continue
    flag = True
    for letter in elem:
        if elem.count(letter) > 1:
            flag = False
            break
    if flag == False:
        continue
    flag = True
    for i in range(len(elem) - 1):
        if (int(elem[i]) + int(elem[i + 1])) % 2 == 0:
            flag = False
    if flag == True:
        ans += 1
print(ans)







