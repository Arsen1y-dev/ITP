## 1.1 Линейные алгоритмы
#
#
#
#
## 	A + B на разных строках (1)
#
#
#a = int(input())
#b = int(input())
#print(a + b)
#
#
#
## Линейные алгоритмы. Задача 2.1 (2)
#
#
#a = int(input())
#b = a % 10
#c = a // 100
#d = a % 100 // 10
#print(b + c + d)
#print(b * c * d)
#
#
#
## 	Линейные алгоритмы. Задача 2.5 (3)
#
#
#N = int(input())
#
#units_digit = str(N % 10)
#
#result = units_digit + str(N)
#
#print(result)
#
#
#
## Часы и минуты (4)
#
#
#k = int(input())
#
#h = k // 3600  # 1 час = 3600 секунд
#k %= 3600
#m = k // 60  # 1 минута = 60 секунд
#
#print(f'It is {h} hours {m} minutes.')
#
#
#
## Путь улитки (5)
#
#
#x1 = int(input())
#x2 = int(input())
#x3 = int(input())
#
## Вычисление суммарной длины пути
#total_distance = abs(x2 - x1) + abs(x3 - x2) + abs(x1 - x3)
#
#print(total_distance)
#
#
#
## Восстановление чисел по сумме и разности (6)
#
#
#a = int(input())
#b = int(input())
#
## Решение системы уравнений
#x = (a + b) // 2
#y = (a - b) // 2
#
#print(x, y)
#
#
#
## Максимальное число квадратов (7)
#
#
#a = int(input())
#b = int(input())
#k = int(input())
#
## Вычисление количества квадратов
#count_a = a // k
#count_b = b // k
#total_count = count_a * count_b
#
#print(total_count)
#
#
#
# Амёбы (8)


N = int(input())

# Вычисление количества амёб
amoebas = 2**(N // 3)


print(amoebas)