n = int(input())
if n == 0:
    print(0)
elif n != 0:
    prevnum = 0
    fibonachi = 1
    for i in range(2, n+1):
        prevnum, fibonachi = fibonachi, prevnum + fibonachi
    print(fibonachi)


nextn = int(input())
numofmore = 0
prevnum = 10**9
while nextn != 0: 
    if nextn > prevnum:
        numofmore = numofmore + 1
    prevnum = nextn
    nextn = int(input())
print(numofmore) 

	Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента




Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.


	n = int(input())
zeros = 0
for i in range (1 , n+1):
    num = int(input())
    if num == 0:
        zeros = zeros + 1
print(zeros)


num = int(input())
localmax = 0
numofmax = 1
while num != 0: 
    if num > localmax: 
        localmax = num
        numofmax = 1
    elif num == localmax:
        numofmax += 1
    num = int(input())
print(numofmax)

numofnum = 0
num = int(input())
while num != 0:
        if num == 0: 
                break
        numofnum = numofnum + 1
        num = int(input())
print(numofnum)



nextnum = int(input())
prevnum = 10**9
localmax = 1
totalmax = 0
while nextnum != 0:
    if nextnum == prevnum:
        localmax = localmax + 1 
    if nextnum != prevnum:
        if localmax > totalmax:
                totalmax = localmax
        localmax = 1
    prevnum = nextnum  
    nextnum = int(input())
if localmax > totalmax:
    totalmax = localmax    
print(totalmax)
            
