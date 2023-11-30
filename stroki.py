a = input()
b = input()
print(len(a))
print(a[::2])
print(a[::-1])
print(a.count(b))


a = input()
b = ''
for i in range(len(a)):  # for i in a
    if a[i].islower():
        b = b + a[i].upper()
    if a[i].isupper():
        b = b + a[i].lower()
print(b)
замена строчных на заглавные и наоборот


s = input()
unders = input()
print(s.find(unders))
print(s.rfind(unders))



s = input()
numofnum = 0
for i in s:
    if i.isdigit():
        numofnum += 1
print(numofnum)




s = input()
sumofnum = 0
for i in s:
    if i.isdigit():
        sumofnum += sumofnum + i
print(sumofnum)



s = input()
numofwords = 1
for i in s:
    if i == ' ':
        numofwords = numofwords + 1
print(numofwords) посчитать количество введенных слов

s = input()
a = s.find("h")
b = s.rfind("h")
print(s[b-1:a:-1]) 
Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную между первым и последним появлением буквы h, в противоположном порядке


s = input()
ans = s.replace("1", "one")
print(ans)
все "1" заменяем на уан


s = input()
ans = s.replace("@", "")
print(ans) 
удалить все собачки из строки

s = input()
ind = 0
if s.count("f") == 1:
    print("-1")
elif s.count("f") == 0:
    print("-2")
else:
    a = s.find("f")
    ind += a + 1
    b = s.find("f", ind)
    ind = b
    print(ind)

Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения. Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2



s = input()
if int(s) < 100:
    print("Oops")        
else:
    print(s[-3])
