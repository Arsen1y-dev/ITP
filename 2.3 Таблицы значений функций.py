## 2.3 Таблицы значений функций 8, 13, 17	
#
#
#
#
## Таблица значений функции 8 (1)
#
#
a, b, h = map(float, input().split())

# Используйте round для точных сравнений с плавающей точкой
a = round(a, 6)
b = round(b, 6)
h = round(h, 6)

# Используйте round для корректного сравнения чисел с плавающей точкой
x = a
while x <= b:
    try:
        y = (3 * x + 4) / ((x**2 + 2 * x + 1) ** 0.5)
        print(f'{x:.6f}\t{y:.6f}')
    except (ValueError, ZeroDivisionError):
        print(f'{x:.6f}\tundefined')
    x = round(x + h, 6)



