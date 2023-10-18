## 1.2 Ветвление
#
#
#
#
## Грузовой автомобиль (1)
#
#
#n = int(input())
#
## Считываем массы предметов и сохраняем их в списке
#masses = []
#for _ in range(n):
#    mass = int(input())
#    masses.append(mass)
#
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
#product = 1.0
#
## Читаем последовательность чисел до первого отрицательного числа
#while True:
#    num = float(input())
#    if num < 0:
#        break
#    product *= num
#
#print(f"{product:.6f}")
#
#
#
## Циклы с параметром. Задача 3 (3)
#
#
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
#print(max_modulus_index)
#
#
#
## ЕГЭ. Задача 6 (4)
#
#
#n = int(input())
#
#current_length = 1
#max_length = 1
#
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
#print(max_length)
#
#
#
## Циклы. Задача 1.5 (5)
#
#
#import math
#
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
#N = int(input())
#
## Cписок для хранения простых множителей
#prime_factors = []
#
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
prev_num = int(input())
current_num = int(input())

if prev_num < current_num:
    sequence_type = "ASCENDING"
elif prev_num > current_num:
    sequence_type = "DESCENDING"
else:
    sequence_type = "CONSTANT"

prev_num = current_num

while True:
    current_num = int(input())
    if current_num == -2 * 10**9:
        break

    if prev_num < current_num:
        if sequence_type == "DESCENDING":
            sequence_type = "RANDOM"
        elif sequence_type == "CONSTANT" or sequence_type == "WEAKLY DESCENDING":
            sequence_type = "WEAKLY ASCENDING"
    elif prev_num > current_num:
        if sequence_type == "ASCENDING":
            sequence_type = "RANDOM"
        elif sequence_type == "CONSTANT" or sequence_type == "WEAKLY ASCENDING":
            sequence_type = "WEAKLY DESCENDING"

    prev_num = current_num

print(sequence_type)
#
#
#
## Максимальный блок (8)
#
#
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
#print(max_sum)




a = []
while True:
    current_num = int(input())
    if current_num == abs(2 * 10**9):
        break
    a.append(current_num)
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        sequence_type = 'DESCENDING'
    elif a[i] < a[i+1]:
        sequence_type = 'ASCENDING'
    elif a[i] == a[i+1]:
        sequence_type = 'CONSTANT'
    elif 


# Вывод результата
print(sequence_type)




prev_num = int(input())
sequence_type = None  

while True:
    current_num = int(input())
    
    
    if current_num == -2 * 10**9:
        break
    
   
    if current_num > prev_num:
        if sequence_type == None or sequence_type == 'ASCENDING' or sequence_type == 'WEAKLY ASCENDING':
            sequence_type = 'ASCENDING'
        else:
            sequence_type = 'RANDOM'
    elif current_num < prev_num:
        if sequence_type == None or sequence_type == 'DESCENDING' or sequence_type == 'WEAKLY DESCENDING':
            sequence_type = 'DESCENDING'
        else:
            sequence_type = 'RANDOM'
    else:
        if sequence_type == None or sequence_type == 'CONSTANT':
            sequence_type = 'CONSTANT'
        elif sequence_type == 'ASCENDING':
            sequence_type = 'WEAKLY ASCENDING'
        elif sequence_type == 'DESCENDING':
            sequence_type = 'WEAKLY DESCENDING'
    
    prev_num = current_num

print(sequence_type)