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
