f = open("text17" , 'r')
arr = list(f.readlines())
numpar = 0 
maxpar = 0
q = 1
m = 0
for i in range(len(arr)):
    if (int(arr[i]) % 2 == 1):
        x += 1
        m += int(arr[i])
    x = m/q
for i in range(len(arr) - 1):
    if (int(arr[i]) % 5 == 0 or int(arr[i+1]) % 5 == 0) and (int(arr[i]) < x or int(arr[i]) < x + 1):
        numpar += 1
    maxpar = max(int(x))
print(numpar , maxpar)




f = open("text17" , "r")
arr = list(f.readlines())
max = -10**9
count = 0
for i in range(len(arr)):
    arr[i] = int(arr[i])
    for j in range(i + 1 , len(arr)):
        arr[j] = int(arr[j])
        if (arr[i] + arr[j]) % 117 == 0:
            count += 1
            if arr[i] + arr[j] > max:
                max = arr[i] + arr[j]
print(count , max)


7 nomer:

f = open("text17" , "r")
arr = list(f.readlines())
maxnum = -10**9
count = 0
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(arr) - 2):
    a = max(arr[i] , arr[i+1] , arr[i+2])
    b = min(arr[i] , arr[i+1] , arr[i+2])
    c = (arr[i] + arr[i+1] + arr[i+2]) - (a + b)
    if b **2 + c ** 2 > a**2:
        count += 1
        if arr[i] + arr[i+1] + arr[i+2] > maxnum:
            maxnum = arr[i] + arr[i+1] + arr[i+2]
print(count  , maxnum)



f = open("text17" , "r")
arr = list(f.readlines())
max = -10**9
count = 0
for i in range(len(arr)):
    arr[i] = int(arr[i])
    for j in range(i + 1 , len(arr)):
        arr[j] = int(arr[j])
        if (arr[i] * arr[j]) % 10 == 0:
            count += 1
            if arr[i] + arr[j] > max:
                max = arr[i] + arr[j]
print(count , max)


f = open("text17" , "r")
arr = list(f.readlines())
max = -10**9
count = 0
for i in range(len(arr)):
    arr[i] = int(arr[i])
    for j in range(i + 1 , len(arr)):
        arr[j] = int(arr[j])
        if (arr[i] + arr[j]) % 10 == 0:
            count += 1
            if arr[i] + arr[j] > max:
                max = arr[i] + arr[j]
print(count , max)

