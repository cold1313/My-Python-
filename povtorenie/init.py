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

