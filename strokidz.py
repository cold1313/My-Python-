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
