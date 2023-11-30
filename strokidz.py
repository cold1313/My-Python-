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
sumofnum = ''
for i in s:
    if i.isdigit():
        sumofnum = sumofnum + i
print(sumofnum)
