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
