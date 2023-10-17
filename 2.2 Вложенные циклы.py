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
#
#
def check_prime(a):
    for x in range(2, int(a ** 0.5) + 1):
        if a % x == 0:
            return False
    return True


def check_prime_divs(a):
    for x in range(2, int(a ** 0.5) + 1):
        if a % x == 0:
            if check_prime(x) and check_prime(a // x):
                return "Yes"
    return "No"

n = int(input())
print(check_prime_divs(n))

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
