arr = [0 for _ in range(1000)]
for i in range(2, 1000):
  if arr[i] == 0:
    for j in range(2*i , 1000, i):
      arr[j] = 1
if arr[8] == 0:
    print("Число простое")
else:
   print("Число не простое")
