def f(x):
  if x <= 2:
    return 2
  if x > 2:
    return f(x-1) + 2 * f(x-2)
print(f(5))




Сколько существует таких чисел n, что 1 ≤ n ≤ 1000 и F(n)  =  3?

count = 0
for x in range(1 , 1000 + 1):
  def f(x):
      if x == 0:
        return 0
      if x > 0 and x % 2 == 0:
        return f(x/2)
      if x % 2 != 0:
        return 1 + f(x-1)
  if f(x) == 3:
    count += 1
print(count)


15 nomer iz dz
def f(x):
    if x == 1:
      return 1
    if x % 2 == 0:
      return x + f(x-1)
    if x > 1 and x % 2 != 0:
      return 2 * f(x-2)
print(f(26))

13 nomer iz dz
def f(x):
  if x == 1:
    return 1
  if x == 2:
    return 2
  if x > 2:
    return f(x-2) * (x-1)
print(f(8)) 

12 nomer iz dz
def f(x):
  if x <= 2:
    return x + 4
  if x > 2:
    return f(x-1) + f(x-2)
print(f(6))


8 nomer:

def f(x):
  if x < 3:
    return 1
  if x > 2 and x % 2 != 0:
    return f(x-1) + 3 * f(x-2)
  if x > 2 and x % 2 == 0:
    sum = 0
    for i in range (1 , x):
      sum += f(i)
    return sum

print(f(28))


