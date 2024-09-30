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
