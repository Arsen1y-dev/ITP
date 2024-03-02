from math import log, sqrt

a, b, h = map(float, input().split())

a = round(a, 6)
b = round(b, 6)
h = round(h, 6)

if a == 1:
    print(f'{a:.6f}\tundefined')
else:
    x = a
    while x <= b:
        if x > 2:
            y = log(x - 2) / sqrt(5 * x + 1)
            print(f'{x:.6f}\t{y:.6f}')
        else:
            print(f'{x:.6f}\tundefined')
        x = round(x + h, 6)
