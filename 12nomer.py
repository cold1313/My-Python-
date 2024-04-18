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
