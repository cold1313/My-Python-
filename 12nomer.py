s = "1" + 100 * "9"
while "19" in s or "299" in s or "3999" in s:
    s = s.replace("19" , "2" , 1)
    s = s.replace("299" , "3" , 1)
    s = s.replace("3999" , "1" , 1)
print(s) 





arr = [0 for _ in range(1000)]
for i in range(2, 1000):
  if arr[i] == 0:
    for j in range(2*i , 1000, i):
      arr[j] = 1

for i in range(41, 1000):
        x = "0" + "1" * 40 + "2" * i + "0"
        while "00" not in x:
            x = x.replace('02' , '101' , 1)
            x = x.replace('11' , '2' , 1)
            x = x.replace('012' , '30' , 1)
            x = x.replace('010' , '00' , 1)
        sum = 0
        for j in x:
            sum += int(j)
        if arr[sum] == 0:
            print(i)
            break


s = "1" + 80 *  '8'
while "18" in s or "288" in s or "3888" in s:
    if "18" in s:
        s = s.replace("18" , "2" , 1)
    elif "288" in s:
        s = s.replace("288" , "3" , 1)
    else:
        s = s.replace("3888" , "1" , 1)
print(s)


s = "0" + 12 * "1" + 15 * "2" + 17 * "3"
while "01" in s or "02" in s or "03" in s:
    s = s.replace("01" , "20" , 1)
    s = s.replace("02" , "120" , 1)
    s = s.replace("03" , '302' , 1)
count = 0
for i in range(len(s)):
    if s[i] == "1":
        count += 1
print(count)


s = ">" + 26 * "1" + 10 * "2" + 14 * "3"
while ">1" in s or ">2" in s or ">3" in s:
    if ">1" in s:
        s = s.replace (">1" , "22>" , 1)
    if ">2" in s:
        s = s.replace (">2" , "2>" , 1)
    if ">3" in s:
        s = s.replace (">3" , "1>" , 1)
count_1 = 0
count_2 = 0
count_3 = 0
for i in range(len(s)):
    if s[i] == "1":
        count_1 += 1
    if s[i] == "2":
        count_2 += 1
    if s[i] == "3":
        count_3 += 1
print(count_1 , count_2 , count_3)


for i in range(3 , 100001):
    s = "5" + "2" * i
    while "52" in s or "1122" in s or "2222" in s:
        if "52" in s:
            s = s.replace("52" , "1" , 1)
        if "2222" in s:
            s = s.replace("2222" , "5" , 1)
        if "1122" in s:
            s = s.replace("1122" , "25" , 1)
    if 1*s.count("1")+2*s.count("2")+5*s.count("5") == 88:
        print(i)
        break
