
n = int(input())
for i in range (n):
    num1, num2 = map(int, input().split('; '))
    print(min(num1 , num2))  
минимум из н пар чисел 


n = int(input())
sumofnum = 0
for i in range (n):
    sumofnum = sumofnum + i + 1
print(sumofnum) 
сумма чисел от 1 до н (3 = 6) 


n = int(input())
sumofnum = 0
for i in range (n):
    sumofnum = sumofnum + 1/(i+1)
print(sumofnum) 
(посчитайте сумму чисел от 1 + 1/2  до 1/н)


a, b = map(int, input().split())
for i in range (a, b+1):
    if i%2 == 1:
        print(i) 
(вывести нечетные числа в диапазоне от а до и включительно)  



a, b = map(int, input().split())
a = a + (a+1)%2 
for i in range (a, b+1, 2):
    print(i) 
( Гарантируется, что a < b. Выведите все нечетные числа в диапазоне от a до b включительно) 


n = int(input())
cubesum = 0
for i in range (n):
    cubesum = cubesum + (i+1)**3
print(cubesum) 
(По данному натуральному n выведите сумму кубов: 1^3 + 2^3 + … + n^3) 



n = int(input())
minofnum = 1000000000
for i in range (n):
    num = int(input())
    if num < minofnum:
        minofnum = num
print(minofnum) 
(Вводится натуральное число n. Затем вводится n целых чисел. Выведите минимальное число среди всех.) 


n = int(input())
maxnum = 0
indexofmax = 0
for i in range (n):
    num = int(input())
    if num > maxnum:
        maxnum = num
        indexofmax = i
print(indexofmax) 
( Вводится натуральное n. Затем вводится n целых чисел. Выведите индекс максимального числа. ) 



n = int(input())
maxnum = -10**9
secondmax = -10**9
for i in range (n):
    num = int(input())
    if num > maxnum:
        secondmax = maxnum
        maxnum = num
    elif num > secondmax:
        secondmax = num 
print(secondmax) 
( Вводится натуральное n. Затем вводится n целых чисел. Выведите второй максимум среди заданных чисел. ) 






          
    











