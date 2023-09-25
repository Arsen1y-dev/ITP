#name = 'пользователь'
#print('Добрый день,', name, '.', sep = '')
#
#print(5,7,8, sep='\n')
#
#print(5,7,8)
#print(9)
#
#print(5,7,8, end = '')
#print(9)
#
#name = 'пользователь'
#print(f'Добрый день, {name}' )
#
#x = 10
#y = 5
#print(f'{x} * {y} / 2 = {x*y/2}')
#
#print(f'{123:0>9}')
#
#print(f'{123:0<9}')
#
#print(f'{123:0^9}')
#
##int - преобразует строку в целое число
#
## float - преобразует строку в вещественное число
#
## % - остаток от деления
#
## / - деление
#
## // - целочисленное деление 
#
## ** - возведение в степень 
#
## 123 % 10 = 3
#
## 123 // 10 = 12
#
#
#
#
#
#
##1.1 Линейные алгоритмы
#
#
#
#
#
## 	A + B на разных строках
#
#
#a = int(input())
#b = int(input())
#print(a + b)
#
## Линейные алгоритмы. Задача 2.1
#
#
#a = int(input())
#b = a % 10
#c = a // 100
#d = a % 100 // 10
#print(b + c + d)
#print(b * c * d)
#
## 	Линейные алгоритмы. Задача 2.5
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
## Часы и минуты
#
#
## Ввод количества секунд k
#k = int(input())
#
## Рассчитываем количество часов и минут
#h = k // 3600  # 1 час = 3600 секунд
#k %= 3600
#m = k // 60  # 1 минута = 60 секунд
#
## Вывод результата
#print(f'It is {h} hours {m} minutes.')
#
#
#
## Путь улитки
#
#
## Ввод координат точек
#x1 = int(input())
#x2 = int(input())
#x3 = int(input())
#
## Вычисление суммарной длины пути
#total_distance = abs(x2 - x1) + abs(x3 - x2) + abs(x1 - x3)
#
## Вывод результата
#print(total_distance)
#
#
#
## Восстановление чисел по сумме и разности
#
#
## Ввод суммы и разности
#a = int(input())
#b = int(input())
#
## Решение системы уравнений
#x = (a + b) // 2
#y = (a - b) // 2
#
## Вывод результата
#print(x, y)
#
#
#
## Максимальное число квадратов
#
#
## Ввод размеров листа бумаги и длины стороны квадрата
#a = int(input())
#b = int(input())
#k = int(input())
#
## Вычисление количества квадратов
#count_a = a // k
#count_b = b // k
#total_count = count_a * count_b
#
## Вывод результата
#print(total_count)
#
#
#
## Амёбы
#
#
## Ввод количества часов N
#N = int(input())
#
## Вычисление количества амёб
#amoebas = 2**(N // 3)
#
## Вывод результата
#print(amoebas)
#
#
#
#
#
##1.2 Ветвление
#
#
#
#
## Плотность тела
#
#
## Ввод данных
#V1 = int(input())
#m1 = int(input())
#V2 = int(input())
#m2 = int(input())
#
## Вычисляем плотности
#density1 = m1 / V1
#density2 = m2 / V2
#
## Сравниваем плотности и выводим результат
#if density1 > density2:
#    print(1)
#elif density2 > density1:
#    print(2)
#else:
#    print("=")
#
#
#
##Високосный год
#
#
## Ввод года
#y = int(input())
#
## Проверка, является ли год високосным
#if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#    print(29)  # Год високосный, в феврале 29 дней
#else:
#    print(28)  # Год не високосный, в феврале 28 дней
#
#
#
## Вася и работа
#
#
#n = int(input())
#
#if (n % 3 == 0) and (n % 10 == 3):
#    print('0')  
#elif n % 3 == 0:
#    print('1')  
#elif n % 10 == 3:
#    print('1')
#else:
#    print('0')
#
#
## Области. Задача 7
#
#
#x, y = map(float, input().split())
#
#if x >= 2:
#    print("Yes")
#elif 0.5 <= y <= 1.5:
#    print("Yes")
#else:
#    print("No")
#
#
#
#
# Улитка на координатной прямой


#s = input().split()
#x1 = int(s[0])
#x2 = int(s[1])
#x3 = int(s[2])
#res = 0
#if abs(x1 - x2) > abs(x1 - x3):
#    res = res + abs(x1 - x3)
#    res = res + abs(x3 - x2)
#else:
#    res = res + abs(x1 - x2)
#    res = res + abs(x2 - x3)
#print(res)
#
#
#
## Бассейн
#
#

# n = int(input()) 
# m = int(input()) 
# x = int(input()) 
# y = int(input()) 
# 
# len_short = min(n, m) 
# len_long = max(n, m) 
# 
# dist_to_short = min(x, len_short - x) 
# dist_to_long = min(y, len_long - y) 
# 
# print(min(dist_to_short, dist_to_long)) 

#
#
## Сундук с сокровищами
#
#
# a = int(input()) 
# b = int(input()) 
# c = int(input()) 
# d = int(input()) ** 2 
# 
# diag1 = a ** 2 + b ** 2 
# diag2 = a ** 2 + c ** 2 
# diag3 = b ** 2 + c ** 2 
# 
# if diag1 <= d or diag2 <= d or diag3 <= d: 
#     print("Yes") 
# else: 
#     print("No") 
#
#
#
## Возраст
#
#
#k = int(input())
#
# k = int(input()) 
# 
# if 10 <= (k % 100) <= 19: 
#     print(f"Мне {k} лет") 
# elif k % 10 == 1: 
#     print(f"Мне {k} год") 
# elif 2 <= (k % 10) <= 4: 
#     print(f"Мне {k} года") 
# else: 
#     print(f"Мне {k} лет")
#
#
#
