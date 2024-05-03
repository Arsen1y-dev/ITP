def numbers_in_both_strings():
    with open("/Users/arseniy/Documents/GitHub/ITP/2 Семестр/input.txt", "r") as file:
        numbers_list = []
        for line in file:
            if line.strip():
                numbers = [int(num) for num in line.split()]
                numbers_list.append(numbers)
            else:
                numbers_list.append([])

    def find_pairs(func):
        results = []
        for a, b in zip(numbers_list, numbers_list[1:]):
            results.append(func(a, b))
        return results

    return find_pairs(lambda a, b: [x for x in set(a).intersection(set(b)) if a.count(x) == 1 and b.count(x) == 1])

print(numbers_in_both_strings())







#1. Открывается файл "input.txt", который содержит числа в формате, разделенном пробелами.
#2. Числа из каждой строки файла считываются и добавляются в список numbers_list. Если строка пустая, добавляется пустой список.
#3. Создается функция find_pairs, которая принимает другую функцию func в качестве аргумента.
#4. Для каждой пары последовательных списков из numbers_list выполняется функция func, и результаты добавляются в список results.
#5. Возвращается список results, содержащий результаты выполнения функции func для каждой пары последовательных списков из numbers_list.
#6. В данном случае, аргументом для функции find_pairs является лямбда-функция, которая находит пересечение множеств чисел из двух списков (a и b), при условии, что число встречается только один раз в каждом из списков.