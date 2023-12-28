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
