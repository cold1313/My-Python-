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
