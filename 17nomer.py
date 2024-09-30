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
    if (len(arr[i]) == 4 and len(arr[i + 1]) != 4 and len(arr[i + 2]) != 4
            or len(arr[i]) != 4 and len(arr[i + 1]) == 4 and len(arr[i + 2]) != 4
            or len(arr[i]) != 4 and len(arr[i + 1]) != 4 and len(arr[i + 2]) == 4):
        if int(arr[i]) + int(arr[i + 1]) + int(arr[i + 2]) < max15:
            cnt += 1
            if int(arr[i]) + int(arr[i + 1]) + int(arr[i + 2]) < summ:
                summ = int(arr[i]) + int(arr[i + 1]) + int(arr[i + 2])
print(cnt, summ)
