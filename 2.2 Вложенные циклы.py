## 2.2 Вложенные циклы
#
#
#
#
## Максимальное количество делителей (1)
#
#
#def count_divisors(num):
#    count = 0
#    for i in range(1, num + 1):
#        if num % i == 0:
#            count += 1
#    return count
#
#a, b = map(int, input().split())
#max_divisor_count = 0
#result = 0
#
#for num in range(a, b + 1):
#    divisors = count_divisors(num)
#    if divisors > max_divisor_count:
#        max_divisor_count = divisors
#        result = num
#    elif divisors == max_divisor_count:
#        result = max(result, num)
#
#print(result)
#
#
#
## Вложенные циклы. Задача 1.1 (2)
#
#
## Функция для проверки числа на простоту
#def is_prime(num):
#    if num <= 1:
#        return False
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            return False
#    return True
#
#A, B = map(int, input().split())
#
#
#for number in range(A, B + 1):
#    if is_prime(number):
#        print(number, end=' ')
#
#
#
## Вложенные циклы. Задача 1.2 (3)


# Функция для проверки, является ли число простым
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


N = int(input())

# Перебираем числа от 2 до N // 2 и проверяем, можно ли разложить N на два простых множителя
for i in range(2, N // 2 + 1):
    if is_prime(i) and is_prime(N // i):
        print("Yes")
        break
else:
    print("No")
#
#
#
## Вложенные циклы. Задача 1.7 (4)
#
#
# Функция для проверки, является ли число простым
#def is_prime(num):
#    if num <= 1:
#        return False
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            return False
#    return True
#
#N = int(input())
#
## Проверяем, является ли N простым числом
#if is_prime(N):
#    print(N)
#else:
#    # Ищем ближайшее простое число, двигаясь в обе стороны от N
#    lower_prime = N - 1
#    while not is_prime(lower_prime):
#        lower_prime -= 1
#
#    upper_prime = N + 1
#    while not is_prime(upper_prime):
#        upper_prime += 1
#
#    # Определяем, какое из найденных простых чисел ближе к N
#    if N - lower_prime <= upper_prime - N:
#        print(lower_prime)
#    else:
#        print(upper_prime)
