Запись Повтори k [Команда1 Команда2 … КомандаS] означает, что последовательность из S команд повторится k раз.

Черепахе был дан для исполнения следующий алгоритм: Повтори 7 [Вперёд 10 Направо 120].

Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.

cnt = 0
for x in range(1 , 11):
    for y in range(1 , 11):
        if x / 3**0.5 < y < -x / 3 ** 0.5 + 10:
            cnt += 1
print(cnt)


Повтори 4 [Вперёд 12 Направо 90]

Повтори 3 [Вперёд 12 Направо 120].

Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом Повтори 4 [Вперёд 12 Направо 90], и находиться вне области, ограниченной линией, заданной данным алгоритмом: Повтори 3 [Вперёд 12 Направо 120]. Точки на линии учитывать не следует.


cnt = 0
for x in range(1 , 12):
    for y in range(1 , 12):
        if -x/3**0.5 + 12 < y or y < x / 3 ** 0.5:
            cnt += 1
print(cnt)


for x in range(100):
    if (x + 7 + 1) * (x + 7 + 1) > 900: 
        print(x)
        break



for x in range(100):
    if (x + 3 + 1) * (x + 3 + 1) > 400:
        print(x)
        break
