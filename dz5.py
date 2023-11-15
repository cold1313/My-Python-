n = int(input())
if n == 0:
    print(0)
prevnum = 0
fibonachi = 1
for i in range(2, n+1):
     prevnum, fibonachi = fibonachi, prevnum + fibonachi
print(fibonachi)

n = int(input())
numofmore = 0
while n != 0: 
    nextn = int(input())
    if nextn != 0 and nextn > n: 
        numofmore = numofmore + 1
    nextn = n
print(numofmore)

	Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента
