
n = int(input())
a, b = 1, 2  # a=1, b=2
print(a, b)
for i in range (n):
    num1, num2 = map(int, input().split('; '))
    print(min(num1 , num2))   минимум из н пар чисел 


n = int(input())
sumofnum = 0
for i in range (n):
    sumofnum = sumofnum + i + 1
print(sumofnum) сумма чисел от 1 до н (3 = 6) 


n = int(input())
sumofnum = 0
for i in range (n):
    sumofnum = sumofnum + 1/(i+1)
print(sumofnum) (посчитайте сумму чисел от 1 + 1/2  до 1/н)












