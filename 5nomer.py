for i in range (1 , 100000):
    x = bin(i)[2:]
    sum = 0
    for j in range(len(x)):
        sum += int(x[j])
    x += str(sum%2)
    second_sum = 0
    for j in range(len(x)):
        second_sum += int(x[j])
    x += str(second_sum%2)
    y = int(x , 2)
    if y > 83:
        print(y)
        break


for i in range (1 , 10000):
    x = bin(i)[2:]
    x = str(x)
    x += x[-1]
    sum = 0
    for j in range (len(x)):
        sum += int(x[j])
    x += str(sum%2)
    y = int(x , 2)
    if y > 105:
        print(y)
        break


for i in range(1000 , 10000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    third = int(x[2]) + int(x[3])
    second_max = str(first + second + third - max(first , second , third) - min(first , second , third))
    max = str(max(first , second , third))
    ans = second_max + max
    if ans == "1215":
        print(i)
        break
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


for i in range (10000 , 100000):
    x = str(i)
    first = int(x[0]) + int(x[2]) + int(x[4])
    second = int(x[1]) + int(x[3])
    if first >= second:
        y = str(second) + str(first)
    else:
        y = str(first) + str(second)
    if y == "723":
        print(i)
        break



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


            
x = '1140'
y = 0
for i in range (len(x)):
  y += int(x[i])
print(y) # посчитать сумму цифр числа 


for i in range (100 , 1000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    if first > second:
        y = str(second) + str(first)
    else:
        y = str(first) + str(second)
    if y == "1115":
        print(i)
        break


for i in range (1000 , 10000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    third = int(x[2]) + int(x[3])
    max_num = max(first , second , third)
    second_max = (first + second + third) - max_num - min(first , second , third )
    y = str(second_max) + str(max_num)
    if y == "613":
        print(i)
        break

for i in range (1 , 100000):
    x = bin(i)[2:]
    sum = 0
    for j in range (len(x)):
        sum += int(x[j])
    x += str(sum%2)
    second_sum = 0
    for j in range (len(x)):
        second_sum += int(x[j])
    x += str(second_sum%2)
    if int(x , 2) > 77:
        print(i)
        break


24 nomer:

for i in range (2 , 100000):
    x = bin(i)[2:]
    num_of_one = 0
    num_of_zero = 0
    for j in range(len(x)):
        if j%2 == 0 and x[j] == "0":
            num_of_zero += 1
        if j%2 != 0 and x[j] == "1":
            num_of_one += 1
    y = abs(num_of_one - num_of_zero)
    if y == 5:
        print(i)
        break

for i in range (1000 , 10000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    third = int(x[2]) + int(x[3])
    first_max = max(first, second, third)
    second_max = (first + second + third) - (first_max + min(first, second, third))
    y = str(second_max) + str(first_max)
    if y == "1515":
        print(i)


перевод из 10-тичной в 3-ичную
x = int(input())
x_v_troichnoy = ""
while x > 0:
    x_v_troichnoy += str(x%3)
    x//= 3
x_v_troichnoy = x_v_troichnoy[::-1]


for i in range (1000 , 10000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    third = int(x[2]) + int(x[3])
    first_max = max(first , second , third)
    second_max = (first + second + third) - (first_max + min(first , second , third))
    y = str(first_max) + str(second_max)
    if y == "1418":
        print(i)

for i in range(1 , 256):
    x = bin(i)[2:]
    if len(x) < 8:
        a = 8 - len(x)
        x = a * '0' + x
    new_s = ''
    for j in range(len(x)):
        if x[j] == "0":
            new_s += '1'
        else:
            new_s += '0'
    y = int(new_s , 2)
    ans = y - i
    if ans == 133:
        print(i)



for i in range (2, 100000):
    x = bin(i)[2:]
    x = str(x)
    for i in range(len(x)):
        if i % 2 == 0:
            x += "10"
        if i % 2 != 0:
            x += "01"
        y = int(x , 2)
        if y < 109:
            print(y)
            break 



for i in range (1000 , 10000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    third = int(x[2]) + int(x[3])
    max_num = max(first , second , third)
    second_max = (first + second + third) - max_num - min(first , second , third )
    y = str(second_max) + str(max_num)
    if y == "613":
        print(i)
        break


    for i in range (1000 , 10000):
        x = str(i)
        first = int(x[0]) + int(x[1])
        second = int(x[1]) + int(x[2])
        third = int(x[2]) + int(x[3])
        max_num = str(max(first , second , third))
        second_max = str(((first + second + third) - min(first , second , third) - max(first , second , third)))
        y = max_num + second_max
        if y == "1517":
            print(i)
            break

for i in range (2 , 1000):
    x = bin(i)[2:]
    x = str(x)
    x += x[-1]
    sum = 0
    for j in range(len(x)):
        sum += int(x[j])
    x += str(sum % 2)
    y = int(x  , 2)
    if y > 105:
        print(y)
        break


for i in range (1000):
    x = bin(i)[2:]
    if i % 2 == 0:
        x = "10" + x
    if i % 2 != 0:
        x = "1" + x + "01"
    if int(x , 2) > 516:
        print(i)
        break


for i in range (100 , 1000):
    x = str(i)
    first = int(x[0]) * int(x[1])
    second = int(x[1]) * int(x[2])
    k1 = str(max(first , second))
    k2 = str(min(first , second))
    ans = k2 + k1
    if ans == "621":
        print(i)
