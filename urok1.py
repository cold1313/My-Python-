
n = int(input())
sumofnum = 0 
for i in range(n):
    x = int(input())
    sumofnum = sumofnum + x
print(sumofnumw)    




n = int(input()) 
numof0 = 0
for i in range(n):
    x = int(input())
    if x > 0:
        numof0 = numof0 + 1
print(numof0)




a = int(input()) 
b = int(input())
if a > b:
    for i in range(a, b - 1, -1):
        print(i)
if a < b:
    for i in range(a, b + 1):
        print (i)





a = int(input()) 
multiplyofnum = 1
for i in range(1 , a + 1):
    multiplyofnum = multiplyofnum * i
print(multiplyofnum)
        




a = int(input()) 
b = int(input())
if a%2 != 0:
    a = a + 1 
for i in range (a , b+1, 2):
        print(i)    



a = int(input()) 
multiplyofnum = 1
for i in range(1 , a + 1):
    multiplyofnum = multiplyofnum * i
print(multiplyofnum)



n = int(input())
sumofnum = 0
sumofnot = 0
for i in range(n-1):
    x = int(input())
    sumofnot = sumofnot + x 
for i in range(1,n+1):
    sumofnum += i
print(sumofnum - sumofnot)
        
        
