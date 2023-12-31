## 2.3 Таблицы значений функций 8, 13, 17	
#
#
#
#
## Таблица значений функции 8 (1)
#
#
#a, b, h = map(float, input().split())
#
## Используйте round для точных сравнений с плавающей точкой
#a = round(a, 6)
#b = round(b, 6)
#h = round(h, 6)
#
## Используйте round для корректного сравнения чисел с плавающей точкой
#x = a
#while x <= b:
#    try:
#        y = (3 * x + 4) / ((x**2 + 2 * x + 1) ** 0.5)
#        print(f'{x:.6f}\t{y:.6f}')
#    except (ValueError, ZeroDivisionError):
#        print(f'{x:.6f}\tundefined')
#    x = round(x + h, 6)
# 
#
#
##Таблица значений функции 13 (2)
#
#
##
##
from math import log

def check_if_correct(x):
    return (x - 2) > EPS and (5 * x + 1) > EPS

a, b, h = map(float, input().split(" "))
EPS = 1e-12
x = a

while x - b < EPS:
    if check_if_correct(x):
        y = (log (x-2)) / (5 * x + 1) ** 0.5
        print(f" {x:.6f} {y:.6f}")
    else:
        print(f"{x:.6f} undefined")
    x +=h
#
#
#
##Таблица значений функции 17 (3)
#
#
#from math import sqrt
#
#a, b, h = map(float, input().split())
#
#a = round(a, 6)
#b = round(b, 6)
#h = round(h, 6)
#
#x = a
#while x <= b:
#    try:
#        if x > 2:
#            y = ((x + 4) / x ** 2 - 2) + sqrt(x ** 3 - 1)
#            print(f'{x:.6f}\t{y:.6f}')
#        else:
#            print(f'{x:.6f}\tundefined')
#    except ValueError:
#        print(f'{x:.6f}\tundefined')
#    x = round(x + h, 6)







