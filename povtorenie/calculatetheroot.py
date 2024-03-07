import math as m


def calculate_x(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return[]
    if d == 0:
        x = -b / (2 * a)
        return[x]
    if d > 0:
        x1 = (-b + m.sqrt(d)) / (2 * a)
        x2 = (-b - m.sqrt(d)) / (2 * a)
        return[x1 , x2]

def output(arr):
    if len(arr) == 0:
        print("there is no solution")
    else:
        print(f"result is {arr}")

def main ():
    a, b, c = map(float, input().split())
    ans = calculate_x(a, b, c)
    output(ans)
    
if __name__ == "__main__":
    main()
