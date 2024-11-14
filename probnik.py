for i in range(1 , 10000):
    x = bin(i)[2:]
    x = str(x)
    if i % 2 == 0:
        x += "01"
    if i % 2 != 0:
        x = "1" + x + "1"
    y = int(x , 2)
    if y >= 156:
        print(i)
        break

s = 45 * "8"
while "1111" in s or "8888" in s:
    if "1111" in s:
        s = s.replace('1111' , '88' , 1)
    else:
        s = s.replace('8888' , '11' , 1)
print(s)

