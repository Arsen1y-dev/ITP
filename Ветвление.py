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



# Циклы с параметром. Задача 3 (3)


# Считываем количество чисел
n = int(input())

# Инициализируем переменные для хранения максимального модуля и его индекса
max_modulus = None
max_modulus_index = None

# Считываем числа и находим максимальный модуль
for i in range(1, n + 1):
    number = int(input())
    modulus = abs(number)
    if max_modulus is None or modulus >= max_modulus:
        max_modulus = modulus
        max_modulus_index = i

# Выводим индекс последнего числа с максимальным модулем
print(max_modulus_index)
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