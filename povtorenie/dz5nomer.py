for i in range (10000 , 100000):
    x = str(i)
    first = int(x[0]) + int(x[2]) + int(x[4])
    second = int(x[1]) + int(x[3])
    if first > second:
        y = str(second) + str(first) 
        if int(y) == 621:
            print(i)
            break 


def f(s):
    sum = 0
    for i in range (len(s)):
        sum += int(s[i])
    return sum
for n in range(1, 100):
    s = bin(n)[2:]  
    s = str(s)
    summa = f(s)
    s = s + str(summa % 2)
    summa = f(s)
    s = s + str(summa % 2)
    r = int(s, 2) 
    if r > 97:
        print(n)
        break


for i in range (1000 , 10000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[2]) + int(x[3])
    if first > second:
        y = str(second) + str(first) 
        if int(y) == 117:
            print(i)



for i in range (100, 10000):
    x = bin(i)[2:]
    x = str(x)
    x = x[:-1]
    if i%2 == 0:
        x = x + "01"
    if i%2 != 0:
        x = x + "10"
    y = int(x, 2)
    if y == 2018:
        print(i)

for i in range (100, 1000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    if first >= second:
        y = str(second) + str(first)
    else:
        y = str(first) + str(second)
        if y == "812":
            print(i)
            break
            
x = '1140'
y = 0
for i in range (len(x)):
  y += int(x[i])
print(y) # посчитать сумму цифр числа 
