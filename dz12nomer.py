for i in range(200 , 1000):
    s = "1" * i
    while "111" in s or "222" in s:
        s = s.replace("111" , "22" , 1)
        s = s.replace("222" , "1" , 1)
    if "1" not in s:
        print(i)
        break


s = ">" + 10 * "1" + 20 * "2" + 30 * "3"
while ">1" in s or ">2" in s or ">3" in s:
    if ">1" in s:
        s = s.replace(">1" , "22>" , 1)
    if ">2" in s:
        s = s.replace(">2" , "2>" , 1)
    if ">3" in s:
        s = s.replace(">3" , "1>" , 1)
print(s.count("1") + s.count("2") * 2)


s = "1" * 85
while "11111" in s:
    s = s.replace("111" , "2" , 1)
    s = s.replace("222" , "1" , 1)
print(s)


for i in range(48 , 200):
    s = "0" + 48 * "1" + i * "2" + "0"
    while "00" not in s:
        s = s.replace("02" , "101" , 1)
        s = s.replace("11" , "2" , 1)
        s = s.replace("012" , "30" , 1)
        s = s.replace("010" , "00" , 1)
    if s.count("1") + s.count("2") * 2 + s.count("3") * 3 
    (НУЖНА ПРОВЕРКА ЧИСЛА НА ПРОСТОТУ)


s =  "8" * 82
while "1111" in s or "8888" in s:
    if "1111" in s:
        s = s.replace("1111" , "8" , 1)
    else:
        s = s.replace("8888" , "11" , 1)
print(s)
