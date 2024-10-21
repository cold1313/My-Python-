f = open('test.txt', 'r')
# f = open('test.txt', 'w') - for writing objects into file

arr = list(f.readlines())
max15 = 0
for i in range(len(arr)):
    if abs(int(arr[i])) % 100 == 15:
        if int(arr[i]) > max15:
            max15 = int(arr[i])
print(max15)

cnt = 0
summ = 1e9
for i in range(len(arr) - 2):
    three = [arr[i], arr[i + 1], arr[i + 2]]
    count4 = 0
    for item in three:
        if 999 < abs(int(item)) < 10000:
            count4 += 1

    if count4 == 1 and int(arr[i]) + int(arr[i + 1]) + int(arr[i + 2]) < max15:
        cnt += 1
        if int(arr[i]) + int(arr[i + 1]) + int(arr[i + 2]) < summ:
            summ = int(arr[i]) + int(arr[i + 1]) + int(arr[i + 2])
print(cnt, summ)



f = open('17.txt', 'r')
arr = list(f.readlines())
count = 0
max_count = -10**9
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if (int(arr[i]) + int(arr[j])) % 10 == 0:
            count += 1
            if (int(arr[i]) + int(arr[j])) > max_count:
                max_count = (int(arr[i]) + int(arr[j]))
print(count, max_count)


f = open('text17' , 'r')
arr = list(f.readlines())
count = 0
max_count = -10**9
for i in range(len(arr)):
    for j in range(i+1 , len(arr)):
        if (int(arr[i]) + int(arr[j])) % 7 == 0:
            count += 1
            if (int(arr[i]) + int(arr[j])) > max_count:
                max_count = (int(arr[i]) + int(arr[j]))
print(count , max_count)


f = open("text17" , "r")
arr = list(f.readlines())
numofpar = 0
maxpara = -10**9
for i in range(len(arr)):
    for j in range(i + 1 , len(arr)):
        if (int(arr[i]) - int(arr[j])) % 80 == 0:
            numofpar += 1
            if int(arr[i]) - int(arr[j]) > maxpara:
                maxpara = int(arr[i]) - int(arr[j])
print(numofpar , maxpara)
        

f = open("text17" , "r")
arr = list(f.readlines())
min = 10 ** 9
count = 0
max = - 10 ** 9
for i in range(len(arr)):
    if int(arr[i]) < min and abs(int(arr[i])) % 10 == 7:
        min = int(arr[i])
for j in range (len(arr) - 1):
    if abs(int(arr[j])) % 10 == 7 and abs(int(arr[j+1])) % 10 != 7 or abs(int(arr[j])) % 10 != 7 and abs(int(arr[j+1])) % 10 == 7:
        if int(arr[j])**2 + int(arr[j+1])**2 < min ** 2:
            count += 1
            if int(arr[j])**2 + int(arr[j+1])**2 > max:
                max = int(arr[j])**2 + int(arr[j+1])**2
print(count , max )

    
