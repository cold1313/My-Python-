arr = [int(x) for x in input().split()] #ввод массива целых чисел
str = ''.join(arr) #преобразовние массива в строку


задача на рекурсию
def f(a):
	if a == 1:
		return 1
	if a == 2:
		return 2
	if a > 2 and a%2 == 0:
		return (3*a + f(a-3))/3
	if a > 2 and a%2 != 0:
		return (7*a + f(a-1) - f(a-2))/5

print(f(35))



for i in range (100, 1000): 
    x = str(i)
    k1 = int(x[0]) * int(x[1])
    k2 = int(x[1]) * int(x[2])
    if k1 > k2:
        s1 = str(k1) + str(k2)
    else:
        s1 = str(k2) + str(k1)
    if s1 == "123":
        print(i)
        break 


for i in range(1, 100):
    s = bin(i)[2:]  
    s = str(s)
    if s.count('1') > s.count('0'):
        s += '1'
    else:
        s += '0'
    r = int(s, 2)
    if r > 80:
        print(r)
        break



for i in range(1, 100):
    s = bin(i)[2:]  
    s = str(s)
    if i % 2 == 0:
        s += '00'
    else:
        s += '11'
    r = int(s, 2) 
    if r > 134:
        print(i)
        break
