my_dict = {}
n = int(input())
for i in range(n):
    arr = list(map(str, input().split()))
    name = arr[0]
    funct = arr[1:]
    my_dict[name] = funct

p = int(input())
for j in range(p):
    arr2 = list(map(str, input().split()))
    if arr2[0] == "read":
        arr2[0] = "R"
    if arr2[0] == "write":
        arr2[0] = "W"
    if arr2[0] == "execute":
        arr2[0] = "X"
    name = arr2[1] 
    if arr2[0] in my_dict[name]:
        print("OK")
    else:
        print("Access denied")


my_dict = {}
array_split = ["," , "." , "!" , "?" , " "]
arr = list(map(str, input().split(array_split)))
for i in arr:
    my_dict[i] = arr.count(i)
count = 10**9
ans = ""
for key, value in my_dict.items():
    if value < count:
        ans = key
        count = value
    elif value == count:
        if key < ans:
            ans = key
print(ans)

    


1. arr = list(map(str, input().split()))
num_of_num = {}

for i in arr:
    i = int(i)  
    if i in num_of_num:
        num_of_num[i] += 1
    else:
        num_of_num[i] = 1

    print(f"(i) - {num_of_num[i]}")

2. Со второй задачей возникла трудность с выводом:

def count(text):
    ans = []
    counts = {}

for j in text:
    if j in counts:
        counts[j] += 1
    else:
        counts[j] = 1

3. n = int(input())
synonym = {}

for i in range(n):
    a , b = input().split()
    synonym[a] = b
    synonym[b] = a
    
x = input()

print(synonym[x])




