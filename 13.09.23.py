name = 'пользователь'
print('Добрый день,', name, '.', sep = '')

print(5,7,8, sep='\n')

print(5,7,8)
print(9)

print(5,7,8, end = '')
print(9)

name = 'пользователь'
print(f'Добрый день, {name}' )

x = 10
y = 5
print(f'{x} * {y} / 2 = {x*y/2}')

print(f'{123:0>9}')

print(f'{123:0<9}')

print(f'{123:0^9}')

#int - преобразует строку в целое число

# float - преобразует строку в вещественное число

# % - остаток от деления

# / - деление

# // - целочисленное деление 

# ** - возведение в степень 

# 123 % 10 = 3

# 123 // 10 = 12

# Задача 1

a = int(input())
b = int(input())
print(a + b)

# Задача 2.1

a = int(input())
b = a % 10
c = a // 100
d = a % 100 // 10
print(b + c + d)
print(b * c * d)

# Задача 2.5


N = int(input())

units_digit = str(N % 10)

result = units_digit + str(N)

print(result)

# Часы и минуты

k = int(input())
h = k // 3600  
k %= 3600
m = k // 60  
print(f'It is {h} hours {m} minutes.')


# Путь улитки

x1 = int(input())
x2 = int(input())
x3 = int(input())

total_distance = abs(x2 - x1) + abs(x3 - x2) + abs(x1 - x3)

print(total_distance)


# Восстановление чисел по сумме и разности

a = int(input())
b = int(input())

x = (a + b) // 2
y = (a - b) // 2

print(x, y)

# Максимальное число квадратов


a = int(input())
b = int(input())
k = int(input())

count_a = a // k
count_b = b // k
total_count = count_a * count_b

print(total_count)

# Амёбы


N = int(input())

amoebas = 2**(N // 3)

print(amoebas)

# Ввод данных
V1 = int(input())
m1 = int(input())
V2 = int(input())
m2 = int(input())

# Вычисляем плотности
density1 = m1 / V1
density2 = m2 / V2

# Сравниваем плотности и выводим результат
if density1 > density2:
    print(1)
elif density2 > density1:
    print(2)
else:
    print("=")
