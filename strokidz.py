s = input()
for i in range(len(s)):
    print(s[i]*(i+1))


s = input()
s1 = ''
numofunique = 0
for i in s: 
	if i not in s1: 
		numofunique = numofunique + 1
		s1 += i
print(numofunique)
print(s1)



s = input()
a = 0
ans = 0
for i in s:
    if i.isdigit():
        a = a*10 + int(i)
    else:
        if a != 0:
            ans = ans + a
        a = 0
if a != 0:
    ans = ans + a        
print(ans)






x = input()
y = x[::-1]
if x == y:
    print("YES")
else: 
    print("NO")

x = float(input())
print(int(x/360 * 12) , int(x/360 * 720%60), int(x/360 * 43200%60))



x = int(input())
y = int(input())
print((x**2 + y**2)**0.5)

n = int(input())
x = "a+b"
if n < 0:
    print(-1)
elif n == 0:
    print(1)
else:
    print(x)**n

