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



Алгоритм получает на вход натуральное число N и строит по нему новое число R следующим образом:

1.  Строится двоичная запись числа N.

2.  В конец двоичной записи добавляются две цифры, соответствующие двоичной записи остатка от деления исходного числа на 3.

3.  В конец двоичной записи числа, полученного на предыдущем шаге, добавляются три цифры, соответствующие двоичной записи остатка от деления этого числа на 5.

4.  Результатом работы алгоритма становится десятичная запись полученного числа R.

 

Пример. Дано число N  =  13. Алгоритм работает следующим образом:

1.  Строим двоичную запись: 1310  =  11012.

2.  Остаток от деления 13 на 3 равен 1, добавляем к двоичной записи цифры 01, получаем 1101012  =  5310.

3.  Остаток от деления 53 на 5 равен 3, добавляем к двоичной записи цифры 011, получаем 1101010112 = 42710.

4.  Результат работы алгоритма R  =  427.

Определите количество принадлежащих отрезку [1 222 222 222; 1 555 555 666] чисел, которые могут получиться в результате работы этого алгоритма.

cnt = 0
x = bin(1555555666)[2:]
x = int(x[:-5] , 2)
y = bin(1222222222)[2:]
y = int(y[:-5] , 2)
print(x-y)


8 nomer iz dz
for i in range(1000, 10000):
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    third = int(x[2]) + int(x[3])
    
    maximum = max(first , second , third)
    secondmax = (first + second + third) - (max(first , second , third)) - (min(first , second , third))

    y = str(secondmax) + str(maximum)
    if int(y) == 1418:
        print(i)
        break


9 nomer iz dz 
for i in range(100, 1000):
    y = 0
    x = str(i)
    first = int(x[0]) + int(x[1])
    second = int(x[1]) + int(x[2])
    
    if second > first:
        y = str(second) + str(first)
    
    if int(y) == 159:
        print(i)
        break
