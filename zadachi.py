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
    
