import argparse
import csv
import math
import sys
import os

# Функция для чтения содержимого CSV-файла
def read_csv_file(file_path):
    if not os.path.isfile(file_path):  # Проверяем, существует ли файл
        raise FileNotFoundError(f"Файл {file_path} не найден")
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]  # Читаем все строки файла в список
        return data
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла {file_path}: {e}")

# Функция для запроса ввода у пользователя
def get_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None

# Функция для разбора аргументов командной строки
def parse_arguments():
    parser = argparse.ArgumentParser(description='Принцип Дирихле')
    parser.add_argument('--file', '-f', default='input.csv', help='Имя CSV-файла')
    parser.add_argument('--number', '-n', type=int, help='Общее число ящиков')
    parser.add_argument('--rows', type=int, help='Количество непустых рядов')
    parser.add_argument('--cols', type=int, help='Количество непустых колонок')
    parser.add_argument('--pigeons', '-m', type=int, help='Число предметов')
    parser.add_argument('items', nargs='*', help='Перечень предметов')
    args = parser.parse_args()

    # Если какие-то параметры не указаны, запросить их у пользователя
    if not args.number:
        args.number = int(get_input("Введите общее число ящиков (number): "))
    if not args.rows:
        args.rows = int(get_input("Введите количество непустых рядов (rows): "))
    if not args.cols:
        args.cols = int(get_input("Введите количество непустых колонок (cols): "))
    if not args.pigeons:
        args.pigeons = int(get_input("Введите число предметов (pigeons): "))
    if not args.items:
        items_input = get_input("Введите предметы через запятую: ")
        if items_input:
            args.items = [item.strip() for item in items_input.split(',')]

    return vars(args)  # Преобразуем аргументы в словарь и возвращаем его

# Функция для проверки корректности параметров
def validate_parameters(params, csv_data):
    errors = []

    n = params.get('number')
    rows = params.get('rows')
    cols = params.get('cols')
    m = params.get('pigeons')

    if n is None or n <= 0:
        errors.append("Параметр 'number' (n) должен быть положительным числом")
    if rows is None or rows <= 0:
        errors.append("Параметр 'rows' должен быть положительным числом")
    if cols is None or cols <= 0:
        errors.append("Параметр 'cols' должен быть положительным числом")
    if m is None or m < 0:
        errors.append("Параметр 'pigeons' (m) должен быть неотрицательным числом")

    total_boxes = len(csv_data) * len(csv_data[0]) if csv_data else 0
    if total_boxes != n:
        errors.append(f"Общее число ящиков (n) должно соответствовать количеству ячеек в CSV-файле ({total_boxes})")

    non_empty_rows = sum(1 for row in csv_data if any(row))
    non_empty_cols = sum(1 for col in zip(*csv_data) if any(col))

    if non_empty_rows != rows:
        errors.append(f"Количество непустых рядов должно быть равно {rows}, но найдено {non_empty_rows}")
    if non_empty_cols != cols:
        errors.append(f"Количество непустых колонок должно быть равно {cols}, но найдено {non_empty_cols}")

    if not errors:
        return True, None  # Если ошибок нет, возвращаем True и None
    else:
        return False, errors  # Если ошибки есть, возвращаем False и список ошибок

# Функция для применения принципа Дирихле
def dirichlet_principle(n, m):
    if m >= n:
        min_items_in_box = math.ceil(m / n)
        return f"Если в {n} ящиках лежит {m} предметов, то хотя бы в одном ящике лежит не менее {min_items_in_box} предметов"
    else:
        empty_boxes = n - m
        return f"Если в {n} ящиках лежит {m} предметов, то пустых ящиков как минимум {empty_boxes}"

# Основная функция программы
def main():
    try:
        params = parse_arguments()
        csv_file = params['file']
        csv_data = read_csv_file(csv_file)

        valid, errors = validate_parameters(params, csv_data)
        if not valid:
            print("Ошибки в параметрах:")
            for error in errors:
                print(f"- {error}")
            sys.exit(1)

        n = params['number']
        m = params['pigeons']

        result = dirichlet_principle(n, m)
        print(result)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()