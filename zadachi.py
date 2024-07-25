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

    
