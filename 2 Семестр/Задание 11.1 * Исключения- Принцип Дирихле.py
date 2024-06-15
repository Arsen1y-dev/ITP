import sys
import csv

def parse_arguments():
    """
    Парсинг аргументов командной строки и ввода через консоль.
    Возвращает словарь параметров.
    """
    params = {}
    
    # Парсинг аргументов командной строки
    for arg in sys.argv[1:]:
        if '=' in arg:
            key, value = arg.split('=')
            params[key.strip()] = value.strip()
    
    # Если параметры не заданы через аргументы командной строки,
    # запрашиваем ввод через консоль
    if not params:
        print("Введите параметры:")
        while True:
            try:
                line = input().strip()
                if line == '':
                    break
                if '=' in line:
                    key, value = line.split('=')
                    params[key.strip()] = value.strip()
                else:
                    params['items'] = line.split(';')
            except KeyboardInterrupt:
                print("\nПрервано пользователем.")
                sys.exit(1)
    
    return params

def read_csv(file_name):
    """
    Чтение содержимого csv-файла.
    Возвращает список списков (строк и столбцов).
    """
    rows = []
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_name} не найден.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при чтении файла {file_name}: {str(e)}")
    
    return rows

def validate_parameters(params):
    """
    Проверка корректности параметров.
    """
    errors = []

    # Проверка наличия и корректности каждого параметра
    if 'file' not in params:
        params['file'] = 'input.csv'
    else:
        try:
            read_csv(params['file'])
        except Exception as e:
            errors.append(f"Ошибка при чтении csv-файла '{params['file']}': {str(e)}")
    
    for param_name in ['n', 'rows', 'cols', 'm']:
        if param_name not in params:
            errors.append(f"Отсутствует обязательный параметр '{param_name}'")
        else:
            try:
                int_value = int(params[param_name])
                if int_value < 0:
                    errors.append(f"Параметр '{param_name}' должен быть положительным числом")
            except ValueError:
                errors.append(f"Параметр '{param_name}' должен быть числом")
    
    # Проверка наличия предметов, если указан параметр 'm'
    if 'm' in params and 'items' in params:
        if len(params['items']) != int(params['m']):
            errors.append(f"Количество предметов ({len(params['items'])}) не соответствует параметру 'm' ({params['m']})")
    
    return errors

def formulate_dirichlet_principle(params, rows):
    """
    Формулировка принципа Дирихле на основе данных.
    """
    n = int(params['n'])
    m = int(params['m'])
    rows_used = int(params['rows'])
    cols_used = int(params['cols'])
    
    if cols_used == 0:
        return "Стеллаж не содержит заполненных столбцов."
    
    # Проверка на одинаковое количество предметов в каждом ящике
    first_box_items = len(rows[0]) if rows else 0
    same_item_count = all(len(row) == first_box_items for row in rows[:rows_used])
    
    if same_item_count and first_box_items == m:
        return f"Все {n} ящиков содержат одинаковое количество предметов: {m}."
    elif m == 0:
        return f"Хотя бы в одном ящике лежит не менее {m+1} предметов."
    else:
        return f"Пустых ящиков как минимум {n - rows_used}."

def main():
    try:
        params = parse_arguments()
        file_name = params.get('file', 'input.csv')
        rows = read_csv(file_name)
        
        errors = validate_parameters(params)
        if errors:
            for error in errors:
                print(error)
            return
        
        principle = formulate_dirichlet_principle(params, rows)
        print(principle)
        
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()