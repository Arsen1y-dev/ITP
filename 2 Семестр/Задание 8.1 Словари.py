"""
Во входном файле задан набор слов и целых чисел, разделённых пробелами. Для каждого слова найти все номера его позиций.
"""

from collections import defaultdict

def index_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Чтение файла и создание списка слов и чисел
        data = ' '.join([line.strip('\n') for line in file.readlines()]).split()
    
    # Создание словаря для хранения позиций слов
    d_index = defaultdict(set)
    
    for i, elem in enumerate(data):
        if elem.isalpha():  # Проверка, является ли элемент словом
            d_index[elem].add(i)
    
    # Возвращаем отсортированный список кортежей (слово, позиции)
    return [(key, sorted(value)) for key, value in d_index.items()]

file_path = '/Users/arseniy/Documents/GitHub/ITP/2 Семестр/input8.1.txt'

result = index_words(file_path)
for word, positions in result:
    print(f"Слово '{word}' найдено на позициях: {positions}")
