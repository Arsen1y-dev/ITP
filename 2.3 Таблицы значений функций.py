## 2.3 Таблицы значений функций 8, 13, 17	
#
#
#
#
## Таблица значений функции 8 (1)
#
#
a, b, h = map(float, input().split())

for x in [round(a + i * h, 6) for i in range(int((b - a) / h) + 1)]:
    try:
        y = (3 * x + 4) /(x**2 + 2 * x + 1)**0.5
        print(f'{x:.6f}\t{y:.6f}')
    except ValueError:
        print(f'{x:.6f}\tundefined')
