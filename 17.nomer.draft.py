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
