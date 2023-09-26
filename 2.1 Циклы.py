## 1.2 Ветвление
#
#
#
#
## Грузовой автомобиль (1)
#
#
## Считываем количество предметов
#n = int(input())
#
## Считываем массы предметов и сохраняем их в списке
#masses = []
#for _ in range(n):
#    mass = int(input())
#    masses.append(mass)
#
## Считываем грузоподъемность автомобиля
#max_capacity = int(input())
#
## Вычисляем общую массу всех предметов
#total_mass = sum(masses)
#
## Проверяем, не превышает ли общая масса грузоподъемность автомобиля
#if total_mass <= max_capacity:
#    print("True")
#else:
#    print("False")
#
#
#
## Циклы. Произведение (2)
#
#
## Инициализируем переменную для хранения произведения
#product = 1.0
#
## Читаем последовательность чисел до первого отрицательного числа
#while True:
#    num = float(input())
#    if num < 0:
#        break
#    product *= num
#
## Выводим произведение с точностью до 6 знаков после десятичной точки
#print(f"{product:.6f}")
#
#
#
## Циклы с параметром. Задача 3 (3)
#
#
## Считываем количество чисел
#n = int(input())
#
## Инициализируем переменные для хранения максимального модуля и его индекса
#max_modulus = None
#max_modulus_index = None
#
## Считываем числа и находим максимальный модуль
#for i in range(1, n + 1):
#    number = int(input())
#    modulus = abs(number)
#    if max_modulus is None or modulus >= max_modulus:
#        max_modulus = modulus
#        max_modulus_index = i
#
## Выводим индекс последнего числа с максимальным модулем
#print(max_modulus_index)
#
#
#
## ЕГЭ. Задача 6 (4)
#
#
## Считываем количество элементов в последовательности
#n = int(input())
#
## Инициализируем переменные для подсчета текущей длины подпоследовательности
#current_length = 1
#max_length = 1
#
## Считываем первый элемент
#prev_element = int(input())
#
## Считываем остальные элементы и проверяем их на равенство предыдущему
#for _ in range(1, n):
#    element = int(input())
#    if element == prev_element:
#        current_length += 1
#    else:
#        current_length = 1
#    prev_element = element
#    if current_length > max_length:
#        max_length = current_length
#
## Выводим наибольшую длину подпоследовательности
#print(max_length)
#
#
#
## Циклы. Задача 1.5 (5)
#
#
#import math
#
## Считываем число N
#N = int(input())
#
## Проверяем, является ли N кубом целого числа
#cube_root = int(round(N ** (1/3)))
#if cube_root ** 3 == N:
#    # Проверяем, является ли cube_root простым числом
#    if cube_root < 2:
#        print("No")
#    else:
#        is_prime = True
#        for i in range(2, int(math.sqrt(cube_root)) + 1):
#            if cube_root % i == 0:
#                is_prime = False
#                break
#        if is_prime:
#            print("Yes")
#        else:
#            print("No")
#else:
#    print("No")
#
#
#
## Циклы. Задача 1.2 (6)
# 
#
## Считываем число N
#N = int(input())
#
## Инициализируем список для хранения простых множителей
#prime_factors = []
#
## Начинаем с наименьшего простого числа (2)
#current_factor = 2
#
#while N > 1:
#    if N % current_factor == 0:
#        # Если N делится на текущий множитель без остатка, добавляем его в список и делим N на него
#        prime_factors.append(current_factor)
#        N //= current_factor
#    else:
#        # Если не делится, переходим к следующему простому числу
#        current_factor += 1
#
## Выводим простые множители в порядке возрастания
#print(" ".join(map(str, prime_factors)))
#
#
#
## Анализ последовательности чисел (7)
#
#

#
#
#
## Максимальный блок (8)
#
#
## Считываем количество чисел в последовательности
#n = int(input())
#
## Считываем первое число
#current_sum = max_sum = int(input())
#
## Проходим по оставшимся числам и находим максимальную сумму подмассива
#for _ in range(1, n):
#    num = int(input())
#    current_sum = max(num, current_sum + num)
#    max_sum = max(max_sum, current_sum)
#
## Выводим максимальную сумму
#print(max_sum)