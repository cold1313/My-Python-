num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 != num2 and num2 != num3 and num3 != num1:
    print ("0")
elif num1 == num2 and num2 == num3:
    print ("3")
else:
    print ("2")




num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 == num3 or num2 == num4 or num2 == num3:
    print ("YES")
else:
    print ("NO")        






num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if abs(num1 - num3) == abs(num2 - num4):
    print ("YES")
else:
    print ("NO")






num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 + num3 == num2 + num4: 
    print ("YES")
else:
    print ("NO")





n = int(input())
sumofnum = 0 
for i in range(n):
    x = int(input())
    sumofnum = sumofnum + x
print(sumofnum)    


