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
for i in range(0 , len(arr)):
        if arr[i] > arr[i - 1]:
            print(arr[i])

a = list(map(int, input().split()))
x = int(input())
place = 0
while place < len(a) and a[place] >= x:
    place += 1
print(place + 1)



arr = list(map(int, input().split()))
for i in range(1, len(arr) , 2):
    arr[i-1] , arr[i] = arr[i] , arr[i-1]
print(arr)



