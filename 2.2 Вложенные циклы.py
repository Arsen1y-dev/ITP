## 2.2 Вложенные циклы
#
#
#
#
## Максимальное количество делителей (1)
#
#
def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

a, b = map(int, input().split())
max_divisor_count = 0
result = 0

for num in range(a, b + 1):
    divisors = count_divisors(num)
    if divisors > max_divisor_count:
        max_divisor_count = divisors
        result = num
    elif divisors == max_divisor_count:
        result = max(result, num)

print(result)
#
#
#
## Вложенные циклы. Задача 1.1 (2)
#
#
# Функция для проверки числа на простоту
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

A, B = map(int, input().split())


for number in range(A, B + 1):
    if is_prime(number):
        print(number, end=' ')

