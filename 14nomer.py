
Значение арифметического выражения: 98 + 35 – 9 – записали в системе счисления с основанием 3. Сколько цифр «2» содержится в этой записи?
x = 9 ** 8 + 3 ** 5 - 9
ans = 0
while x > 0:
    if x%3 == 2:
        ans += 1
    x = x // 3
print(ans) 


Oперанды арифметического выражения записаны в системе счисления с основаниями 13 и 10

8x7113 + 3xDF17

В записи чисел переменной x обозначена неизвестная цифра из алфавита десятичной системы счисления. Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 197. Для найденного значения x вычислите частное от деления значения арифметического выражения на 197 и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.
for i in range (0 , 10):

    a = "8" + str(i) + "71"
    b = "3" + str(i) + "D" + "F"
    x = int(a , 13)
    y = int(b , 17)
    if (x + y)%197 == 0:
        print((x + y) / 197)

1 nomer iz var
x = 16 ** 18 * 4 ** 10 - 4**6 - 16
count = 0
while x > 0:
    if x % 4 == 3:
        count += 1
    x = x // 4
print(count)


for i in range (0 , 15 + 1):
    x = "1" + str(i) + "BAD"
    y = "2" + "C" + str(i) + "FE"
    x = int(x , 16)
    y = int(y , 16)
    ans = x + y
    if ans % 15 == 0:
        print(ans / 15)
        break

x = 4 ** 2020 + 2 ** 2017 - 15
y = bin(x)[2:]
count = 0
for i in range(len(y)):
    if y[i] == "1":
        count += 1
print(count)


for i in range (0 , 8 + 1):
    x = "88" + str(i) + "4" + str(i)
    y = "7" + str(i) + "344"
    rez = int(x , 9) + int(y , 9)
    ans = 0
    if rez % 67 == 0:
        print(rez / 67)

for i in '0123456789ABCD':
    x = "3D4" + i
    y = "4" + i + "C4"
    rez = int(x , 16) + int(y , 14)
    if rez % 154 == 0:
        print(rez / 154)

for i in "0123456789AB":
    for j in "0123456789AB":
        x = i + "231" + j
        y = "78" + i + "98" + j
        rez = int(x , 12) + int(y , 14)
        if rez % 99 == 0:
            print(rez / 99)

for i in "0123456789A":
    for j in "0123456789A":
        x = i + "341" + j
        y = "56" + i + "1" + j
        rez = int(x , 11) + int(y , 19)
        if rez % 305 == 0:
            print(rez / 305)


x = 4 ** 2016 + 2 ** 2015 - 7
y = bin(x)[2:]
count = 0
for i in range(len(y)):
    if y[i] == "1":
        count += 1
print(count) 


Значение выражения 368 + 620 − 12? записали в системе счисления с основанием 6.
Сколько цифр 5 содержится в этой записи?

x = 36 ** 8 + 6 ** 20 - 12
rez = 0
while x > 0:
    if x % 6 == 5:
        rez += 1
    x //= 6
print(rez)

Значение выражения 255 + 514 − 5? записали в системе счисления с основанием 5. Сколько цифр 4 содержится в этой записи?

x = 25 ** 5 + 5 ** 14 - 5
count = 0
while x > 0:
    if x % 5 == 4:
        count += 1
    x //= 5
print(count)


for i in range (0 , 9):
    for j in range(0 , 9):
        x = "88" + str(i) + "4" + str(j)
        y = "7" + str(i) + "44" + str(j)
        a = int(x , 9)
        b = int(y , 11)
        ans = a + b
        if ans % 61 == 0:
            print(ans / 61)
            break


for i in "01233456789ABCDEFGHI":
        x = "78" + str(i) + "79643"
        y = "25" + str(i) + "43"
        z = "63" + str(i) + "5"
        rez = int(x , 19) + int(y , 19) + int(z , 19)
        if rez % 18 == 0:
            print(rez / 18)
            break

for i in range(0 , 8):
    for j in range(0 , 8):
        x = str(i) + "01" + str(j) + "4"
        y = str(i) + str(j) + "544"
        a = int(x , 9)
        b = int(y , 8)
        if (a + b) % 89 == 0:
            print((a + b)/89)
            break
