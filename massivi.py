for i in range (10):
    for j in range(10):
        print((j+1) * (i+1), end = ' ')
    print()
(tablitsa umnozhenia)


n = int(input())
for i in range(n):
    for j in range(n):
        if i == j:
            print( 0 , end = ' ')
        else:
            print(1 , end = ' ')
    print()
диагональ квадрата. НА ДИАГОНАЛИ 0, ОСТАЛЬНОЕ 1



n = int(input())
for i in range(n):
    for j in range(n):
        if i + j == n-1: 
            print(1 , end = ' ')
        else: 
            print(0 , end = ' ')
    print()
  другая диагональ




n = int(input())
arr = []

for i in range(n):
    a = []
    for j in range(n):
        if i == j:
            a.append(0)
        else:
            a.append(1)
    arr.append(a)
for i in range (n):
    for j in range (n):
        print(arr[i][j] , end = ' ')
    print()
опять диагональ




# print(arr.count(max(arr)))
mmax = -1e9
ans = 0
for i in range(len(arr)):
    if mmax < arr[i]:
        mmax = arr[i]
        ans = 1
    elif mmax == arr[i]:
        ans += 1


# ans = 0
# for i in arr:
#     if i == mmax:
#         ans += 1
print(ans)n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)


DZ!!!

arr = list(map(int, input().split()))
for i in range(len(arr)):
        if arr[i] > arr[i - 1]:
            print(arr[i])



переделать 2 задачу
a = list(map(int, input().split()))
x = int(input())
place = 0
while place < len(a) and a[place] >= x:
    place += 1
print(place + 1)



arr = list(map(int, input().split()))
for i in range(1, len(arr) , 2):
    arr[i-1] , arr[i] = arr[i] , arr[i-1]
print(*arr)


4 задача на массивы
arr = list(map(int, input().split()))
k = int(input())
for i in range(len(arr)):
    if i > k:
        arr[i-1] , arr[i] = arr[i] , arr[i-1]
arr.pop()
print(*arr)


1

s = "1" * 77
while s.find("111") != -1:
    s = s.replace("111" , "2")
    s = s.replace("222" , "11")
print(s)



2 = -


3 
s = "9" * 65
while s.find("999") != -1 or s.find("222") != -1:
    if s.find("222"):
        s = s.replace("222" , "9",1)
    else:
        s = s.replace("999" , "2",1)
print(s)  


s = "9" * 65
while ('999' in s) or ('222' in s):
    if '222' in s:
        s=s.replace('222','9',1) 
    else:
        s=s.replace('999','2',1)
print(s)

4
s = "1" + "9" * 98
while ('19' in s) or ('299' in s) or ("3999" in s):
        s=s.replace('19','2',1) 
        s=s.replace('299','3',1)
        s=s.replace('3999','1',1)
print(s)


s = "7" * 85
while ('333' in s) or ("777" in s):
    if "333" in s:    
        s=s.replace('333','7',1)
    else:
         s=s.replace('777','3',1)
print(s)



s = "1" + "9" * 98
while ('19' in s) or ("299" in s) or ("3999" in s):   
        s=s.replace('19','2',1)
        s=s.replace('299','3',1)
        s=s.replace('3999','1',1)
print(s)


2 задача на массивы
arr = list(map(int, input().split()))
n = int(input())
place = 1
for i in range(n):
    if arr[i] >= n:
        place += 1
    else:
        break
print(place)




 for a in range(1, 50):
    for b in range(1, 50):
        for c in range(1, 50):
            string = '0' + a * '1' + b * '2' + c * '3' + '0'
            while '00' not in string:
                string = string.replace('01', '210', 1)
                string = string.replace('02', '320', 1)
                string = string.replace('03', '3012', 1)
            if string.count('1') == 23 and string.count('2') == 48 and string.count('3') == 41:
                print(a + b + c + 2)



nums = list()
target = int(input())
x = []
for i in range(0 , len(nums)-1): 
    if nums[i] + nums[i+1] == target:
        x = [i , i+1]
print(x) 

римские
def (s):
    roman = {
        "I" : 1,
        "V" : 5, 
        "X" : 10, 
        "L" : 50, 
        "C" : 100, 
        "D" : 500, 
        "M" : 1000 
        } 
int = 0
for i in range(len(s) - 1): #цикл до второго с конца, иначе не выполн иф
    if roman[s[i]] < roman[s[i+1]]: #разбор на примере
        int -= roman[s[i]]
    else:
        int += roman[s[i]]
    return int + roman[s[-1]] #добавляем последний элем


l1 = ""
l2 = ""
Solution = 0 
ret = Solution().addTwoNumbers(l1, l2)
print((l1[::-1]) + (l2))

Дана программа для Редактора:

НАЧАЛО

                ПОКА НЕ нашлось (00)

                        заменить (02, 101)

                        заменить (11, 2)

                        заменить (012, 30)

                        заменить (010, 00)

                КОНЕЦ ПОКА

КОНЕЦ

Известно, что исходная строка A содержала ровно два нуля  — на первом и на последнем месте, 40 единиц, больше 40 двоек и не содержала других цифр.

После выполнения данной программы получилась строка B, сумма цифр которой оказалась простым числом. Какое наименьшее количество двоек могло быть в строке A? 
РЕШЕНИЕ 
def Checkstring(string):
    my_sum = 0
    for i in string:
        my_sum += int(i)
    divisers = 0
    for i in range(1, my_sum + 1):
        if my_sum % i == 0: 
            divisers = divisers + 1
    if divisers == 2:
        return True
    else: 
        return False
for i in range(41 , 100):
    x = "0" + "1" * 40 + "2" * i + "0"
    while "00" not in x:
        x=x.replace ("02" , "101" , 1)
        x=x.replace ("11" , "2" , 1)
        x=x.replace ("012" , "30" , 1)
        x=x.replace ("010" , "00" , 1)

    if Checkstring(x):
        print(i)
        break


def Checkstring(x):
    my_sum = 0
    divisers = 0
    for i in x:
        my_sum += int(i)   
    for i in range(1, my_sum + 1):
        if my_sum % i == 0: 
            divisers = divisers + 1
    if divisers == 2:
        return True
    else: 
        return False

ans = 1e9
for a in range(1 , 100):
    for b in range(1, 100):
        x = "0" + "1" * a + "2" * b
        if len(x) > 40:
            while "01" in x or "02" in x:
                x=x.replace ("02" , "1110" , 1)
                x=x.replace ("01" , "220" , 1)
            if Checkstring(x):
                sumofnum = 0
                y = "0" + "1" * a + "2" * b
                for i in y:
                    sumofnum += int(i)
                ans = min(ans, sumofnum)
print(ans)


for i in range(60, 200): 
    x = "1" * i
    while "111" in x: 
        x = x.replace("111" , "2" , 1)
        x= x.replace("222" , "11", 1) 
    if x == "221":
        print(i)
uslovie
Дана программа для Редактора:

НАЧАЛО

ПОКА нашлось (111)

    заменить (111, 2)

    заменить (222, 11)

КОНЕЦ ПОКА

КОНЕЦ

 

К исходной строке, содержащей более 60 единиц и не содержащей других символов, применили приведённую выше программу. В результате получилась строка 221. Какое наименьшее количество единиц могло быть в исходной строке?

for i in range (4, 10000): 
    x = "5" + "2" * i
    while "52" in x or "1122" in x or "2222" in x:
        if "52" in x:
            x = x.replace("52" , "11" , 1)
        if "2222" in x: 
            x = x.replace("2222" , "5" , 1)
        if "1122" in x: 
            x = x.replace("1122" , "25" , 1)
    sumofnum = 0
    for a in x:
        sumofnum += int(a)
    if sumofnum == 64:
        print(i)

Дана программа для Редактора:

НАЧАЛО

  ПОКА нашлось (52) ИЛИ нашлось (1122) ИЛИ нашлось (2222)

     ЕСЛИ нашлось(52)

          ТО заменить (52, 11)

     КОНЕЦ ЕСЛИ

     ЕСЛИ нашлось(2222)

          ТО заменить (2222, 5)

     КОНЕЦ ЕСЛИ

     ЕСЛИ нашлось(1122)

          ТО заменить (1122, 25)

     КОНЕЦ ЕСЛИ

  КОНЕЦ ПОКА

КОНЕЦ

На вход приведённой выше программе поступает строка, начинающаяся с цифры «5», а затем содержащая n цифр «2» (3 < n < 10 000).

Определите наименьшее значение n, при котором сумма цифр в строке, получившейся в результате выполнения программы, равна 64.


