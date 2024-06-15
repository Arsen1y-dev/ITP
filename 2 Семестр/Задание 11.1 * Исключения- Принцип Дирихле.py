import csv
import argparse
import sys

def check_parameters(file_name, num_boxes, rows, cols, num_items, items):
    """
    Проверяет корректность введенных параметров и содержимого CSV-файла.
    """

    errors = []

    # Проверка количества ящиков
    if not isinstance(num_boxes, int) or num_boxes <= 0:
        errors.append(f"Некорректное значение для количества ящиков: {num_boxes}")

    # Проверка размеров стеллажа
    if not isinstance(rows, int) or rows <= 0:
        errors.append(f"Некорректное значение для количества рядов: {rows}")
    if not isinstance(cols, int) or cols <= 0:
        errors.append(f"Некорректное значение для количества колонок: {cols}")

    # Проверка количества предметов
    if not isinstance(num_items, int) or num_items < 0:
        errors.append(f"Некорректное значение для количества предметов: {num_items}")

    # Проверка соответствия количества ящиков и размерам стеллажа
    if num_boxes != rows * cols:
        errors.append(f"Количество ящиков ({num_boxes}) не соответствует размеру стеллажа ({rows} x {cols})")

    # Проверка количества предметов в CSV-файле
    csv_items = None  # Инициализация за пределами блока try
    try:
        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            csv_items = sum(len(row) for row in reader)
    except FileNotFoundError:
        errors.append(f"Файл '{file_name}' не найден")
    except Exception as e:
        errors.append(f"Ошибка при чтении файла '{file_name}': {e}")

    if num_items != csv_items:
        errors.append(f"Количество предметов в CSV-файле ({csv_items}) не соответствует заданному значению ({num_items})")

    return errors

def formulate_principle(num_boxes, num_items):
    """
    Формулирует принцип Дирихле для заданных параметров.
    """

    if num_items >= num_boxes:
        return f"Если в {num_boxes} ящиках лежит {num_items} предметов, то хотя бы в одном ящике лежит не менее {num_items // num_boxes + 1} предметов."
    else:
        return f"Если в {num_boxes} ящиках лежит {num_items} предметов, то пустых ящиков как минимум {num_boxes - num_items}."

def main():
    """
    Основная функция программы.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="input.csv", help="Имя CSV-файла")
    parser.add_argument("-n", "--number", type=int, help="Общее количество ящиков")
    parser.add_argument("-r", "--rows", type=int, help="Количество рядов")
    parser.add_argument("-c", "--cols", type=int, help="Количество колонок")
    parser.add_argument("-m", "--pigeons", type=int, help="Количество предметов")
    parser.add_argument("items", nargs='*', help="Список предметов (разделенных запятыми или точкой с запятой)")

    args = parser.parse_args()

    file_name = args.file
    num_boxes = args.number
    rows = args.rows
    cols = args.cols
    num_items = args.pigeons
    items = args.items

    # Обработка ввода с консоли
    if not all([num_boxes, rows, cols, num_items]):
        print("Введите параметры:")
        while True:
            try:
                input_line = input()
                if not input_line:
                    break
                for param in input_line.split():
                    key, value = param.split('=')
                    if key == "f" or key == "file":
                        file_name = value
                    elif key == "n" or key == "number":
                        num_boxes = int(value)
                    elif key == "r" or key == "rows":
                        rows = int(value)
                    elif key == "c" or key == "cols":
                        cols = int(value)
                    elif key == "m" or key == "pigeons":
                        num_items = int(value)
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")
                continue

    # Проверка параметров и содержимого CSV-файла
    errors = check_parameters(file_name, num_boxes, rows, cols, num_items, items)
    if errors:
        print("Ошибки:")
        for error in errors:
            print(error)
        sys.exit(1)

    # Формулировка принципа Дирихле
    print(formulate_principle(num_boxes, num_items))

if __name__ == "__main__":
    main()