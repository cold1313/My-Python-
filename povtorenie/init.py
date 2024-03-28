arr = [int(x) for x in input().split()] #ввод массива целых чисел
str = ''.join(arr) #преобразовние массива в строку


задача на рекурсию
def f(a):
	if a == 1:
		return 1
	if a == 2:
		return 2
	if a > 2 and a%2 == 0:
		return (3*a + f(a-3))/3
	if a > 2 and a%2 != 0:
		return (7*a + f(a-1) - f(a-2))/5

print(f(35))



for i in range (100, 1000): 
	x = str(i)
    k1 = int(x[0]) * int(x[1])
    k2 = int(x[1]) * int(x[2])
    if k1 > k2:
        s1 = str(k1) + str(k2)
    else:
        s1 = str(k2) + str(k1)
    if s1 == "123":
        print(i)
        break 


for i in range(1, 100):
    s = bin(i)[2:]  
    s = str(s)
    if s.count('1') > s.count('0'):
        s += '1'
    else:
        s += '0'
    r = int(s, 2)
    if r > 80:
        print(r)
        break



for i in range(1, 100):
    s = bin(i)[2:]  
    s = str(s)
    if i % 2 == 0:
        s += '00'
    else:
        s += '11'
    r = int(s, 2) 
    if r > 134:
        print(i)
        break


count = 0
for i in range (1000, 10000): 
    x = str(i)
    k1 = int(x[0]) * int(x[1])
    k2 = int(x[2]) * int(x[3])
    if k1 > k2:
        s1 = str(k1) + str(k2)
    else:
        s1 = str(k2) + str(k1)
    if s1 == "616":
        count += 1
print(count)

 for i in range(1000, 10000):
    s = str(i)
    k1 = int(s[0]) * int(s[1])
    k2 = int(s[2]) * int(s[3])
    first = str(max(k1, k2))
    second = str((min(k1, k2)))
    s1 = first + second
    if s1 == '124':
        print(i)
        break


for i in range(3 , 10001):
    x = "5" + "2" * i
    while "52" in x or "1122" in x or "2222" in x:
            x = x.replace("52" , "1" , 1)
            x = x.replace("2222" , "5" , 1)
            x = x.replace("1122" , "25" , 1)
            for j in x:
                if 1*x.count("1")+2*x.count("2")+5*x.count("5") == 88:
                    print(i)
                    break     



cnt = 0
for i in range(1, 10, 2):
    for j in range(1, 10, 2):
        for k in range(1, 10, 2):
            for h in range(1, 10, 2):
                first = i + j
                second = k + h
                s = ''
                if first < second:
                    s += str(first) + str(second)
                else:
                    s += str(second) + str(first)

                if s == '616':
                    cnt += 1
print(cnt)
