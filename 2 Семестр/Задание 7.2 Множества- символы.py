n = int(input())  # Количество строк

for _ in range(n):
    line = input()
    intersection_set = set()
    
    # Находим буквы в верхнем и нижнем регистре
    for char in line:
        if char.isalpha():
            if char.lower() in intersection_set:  # Если символ уже есть в множестве, то добавляем его в результат
                intersection_set.add(char)
    
    result = sorted(list(intersection_set))  # Сортируем и преобразуем в список для вывода
    print(''.join(result))
