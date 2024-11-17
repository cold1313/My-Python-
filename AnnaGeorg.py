from itertools import *
arr = product("01234567" , repeat = 5)
count1 = 0
count2 = 0
for elem in arr:
    if int(elem[0]) != "0" and elem.count("1") == 0 and int(elem[0]) % 2 == 0 and int(elem[1]) % 2 == 1 and int(elem[2]) % 2 == 0 and int(elem[3]) % 2 == 1 and int(elem[4]) % 2 == 0:
        count1 += 1
    if int(elem[0]) != "0" and elem.count("1") == 0 and int(elem[0]) % 2 == 1 and int(elem[1]) % 2 == 0 and int(elem[2]) % 2 == 1 and int(elem[3]) % 2 == 0 and int(elem[4]) % 2 == 1:
        count2 += 1
print(count1 , count2)
    
from itertools import *
arr = product("СВЕТЛАН" , repeat = 8)
count = 0
for elem in arr:
    if elem.count("С") == 1 and elem.count("В") == 1 and elem.count("Е") == 1 and elem.count("Т") == 1:
        if elem.count("Л") == 1 and elem.count("А") == 2 and elem.count("Н") == 1:
            if elem.count("АА") == 0:
                    count += 1
print(count)


for i in range(1 , 1000):
    s = ">" + 39 * "0" + i * "1" + 39 * "2"
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1" , "22>")
        if ">2" in s:
            s = s.replace('>2' , "2>")
        if ">0" in s:
            s = s.replace(">0" , "1>")
        rez = s.count("2") * 2 + s.count("1")
    m = 0
    for i in range(1 , rez + 1):
        if rez % i == 0:
            m += 1
            if m > 2:
                break
    if m == 2: 
        print(i)
        break


for i in range(4 , 10000):
    s = "8" + "7" * i
    max = -10**9
    while '57' in s or "877" in s or "777" in s:
        if "57" in s:
            s = s.replace("57" , "7" , 1)
        if '877' in s:
            s = s.replace('877' , "75" , 1)
        if "777" in s: 
            s = s.replace("777" , "8" , 1)
        rez = 5 * s.count("5") * 7 * s.count("7") * 8 * s.count("8") 
        if rez > max:
            max = 5 * s.count("5") * 7 * s.count("7") * 8 * s.count("8")
print(max)
