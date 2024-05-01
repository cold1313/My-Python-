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
