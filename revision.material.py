number = int(input())  # get integer from user
floater = float(input())  # get float from user
number += floater  # short for number = number + floater

'''
for many line comments
/ - division
// - int division
% - rest after int division
** - pow
'''

b = number < floater  # bool variable, can be 1 or 0 (True / False)

string = input()  # get string from user
a = str(number)  # convert from smth to str

s0 = string[0]  # put elem from string with index 0 to s0
s14 = string[1:5]  # put substr from string with indexes from 1 to 4 (5 not including) to s14
reverse = string[::-1]  # put reversed string to reverse
ind_left = string.find('smth')
ind_right = string.rfind('smth')
count_smth = string.count('smth')
# and there are other useful function like isdigit ans etc.

if number < floater and len(string) >= len(reverse) or b:  # how if works with many args
    print(f'{number} is less than {floater}')  # fstring, we can put vars into string
elif len(s0) < len(s14):  # if the condition above this is true, this won't work
    print('a')
else:  # without any condition
    print('b')

i = 0
while i < 10:  # while condition is true it will work
    print('f', end='')  # after each print another print starts from new string in console
    # if you want another ending after print you can change it
    i += 1
print()

start = 0
stop = 10
step = 1
for i in range(start, stop, step):  # i = 0, 1, 2, ..., stop-1; on base start = 0, step = 1, stop isn't included
    print(string[i])

for elem in string:  # each element in string
    print(elem)

for i in range(len(string)):  # each index of elements in string
    print(string[i])
