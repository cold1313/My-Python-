n = int(input())
check = True
if n == 1:
    check = False
for i in range (2 , n):
    if n%i == 0:
        check = False
if not check:
    print("NO")
else:
    print("YES")


Вводится натуральное число n. Выведите “YES”, если число является простым, и “NO” в противном случае



a = int(input())
b = int(input())
c = int(input())
if c < a * b and (c%a == 0 or c%b == 0):
    print ('YES')
else: 
    print ('NO')
Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек. Программа получает на вход три числа: n, m, k и должна вывести YES или NO




num  = int(input())
num = num*45 + num//2*5 + ((num+1)//2-1)*15
print(9+ num//60 , num%60)
В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут. Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок. Выведите два целых числа: время окончания урока в часах и минутах.


    
num = int(input())
print(num//10 % 10) 
Дано натуральное число. Найдите число десятков в его десятичной записи.



n = int(input())
notlessthan0 = 0
for i in range (n):
    num = int(input())
    if num == 0:
        notlessthan0 = notlessthan0 + 1
    elif num > 0:
        notlessthan0 = notlessthan0 + 1
    else:
        notlessthan0 = notlessthan0 
print(notlessthan0)
Дано число n. Далее вводится n целых чисел. Выведите количество чисел, не меньших нуля 

    
n = int(input())
factorial = 1
for i in range (1 , n + 1):
    factorial = factorial * i    
print(factorial)    
Вводится натуральное число n. Посчитайте его факториал.



n = int(input())
factorial = 1
sumoffactorial = 0
for i in range (1 , n + 1):
    factorial = factorial * i 
    sumoffactorial = sumoffactorial + factorial
print(sumoffactorial)     
По данному натуральному числу n посчитайте сумму факториалов от 1 до n включительно. Использовать можно только 1 цикл, библиотекой math пользоваться запрещено


