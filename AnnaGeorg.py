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
