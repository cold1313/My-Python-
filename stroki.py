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

    
