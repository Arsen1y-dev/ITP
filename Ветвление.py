# Считываем количество элементов в последовательности
n = int(input())

# Инициализируем переменные для подсчета текущей длины подпоследовательности
current_length = 1
max_length = 1

# Считываем первый элемент
prev_element = int(input())

# Считываем остальные элементы и проверяем их на равенство предыдущему
for _ in range(1, n):
    element = int(input())
    if element == prev_element:
        current_length += 1
    else:
        current_length = 1
    prev_element = element
    if current_length > max_length:
        max_length = current_length

# Выводим наибольшую длину подпоследовательности
print(max_length)