n = int(input())
if n == 0:
    print(0)
prevnum = 0
fibonachi = 1
for i in range(2, n+1):
     prevnum, fibonachi = fibonachi, prevnum + fibonachi
print(fibonachi)

