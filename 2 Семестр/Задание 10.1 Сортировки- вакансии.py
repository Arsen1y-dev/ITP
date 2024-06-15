"""
Считать из файла информацию о вакансиях: фирма, должность, средняя зарплата, необходимый опыт работы. 
Сортировать вакансии пузырьком, выбором (обычным образом и с добавлением устойчивости) и вставками по должности, 
при равенстве по фирме, при равенстве по убыванию опыта работы
"""

import csv

class Vacancy:
    def __init__(self, company, position, salary, experience):
        self.company = company
        self.position = position
        self.salary = salary
        self.experience = experience

    def __str__(self):
        return f"Компания: {self.company}, Должность: {self.position}, Зарплата: {self.salary}, Опыт: {self.experience}"

def read_vacancies(filename):
    """Считывает информацию о вакансиях из CSV-файла.

    Args:
        filename (str): Имя CSV-файла.

    Returns:
        list: Список объектов Vacancy, представляющих вакансии.
    """
    vacancies = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            vacancies.append(Vacancy(row[0], row[1], int(row[2]), int(row[3])))
    return vacancies

def bubble_sort(vacancies):
    """Сортировка пузырьком по должности, затем по фирме, затем по опыту (в убывающем порядке).

    Args:
        vacancies (list): Список объектов Vacancy.

    Returns:
        list: Отсортированный список объектов Vacancy.
    """
    n = len(vacancies)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Сортировка по должности
            if vacancies[j].position > vacancies[j + 1].position:
                vacancies[j], vacancies[j + 1] = vacancies[j + 1], vacancies[j]
            # Сортировка по компании (если должности одинаковые)
            elif vacancies[j].position == vacancies[j + 1].position and vacancies[j].company > vacancies[j + 1].company:
                vacancies[j], vacancies[j + 1] = vacancies[j + 1], vacancies[j]
            # Сортировка по опыту (если должности и компании одинаковые)
            elif vacancies[j].position == vacancies[j + 1].position and vacancies[j].company == vacancies[j + 1].company and vacancies[j].experience < vacancies[j + 1].experience:
                vacancies[j], vacancies[j + 1] = vacancies[j + 1], vacancies[j]
    return vacancies

def selection_sort(vacancies):
    """Сортировка выбором по должности, затем по фирме, затем по опыту (в убывающем порядке).

    Args:
        vacancies (list): Список объектов Vacancy.

    Returns:
        list: Отсортированный список объектов Vacancy.
    """
    n = len(vacancies)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Сортировка по должности
            if vacancies[min_idx].position > vacancies[j].position:
                min_idx = j
            # Сортировка по компании (если должности одинаковые)
            elif vacancies[min_idx].position == vacancies[j].position and vacancies[min_idx].company > vacancies[j].company:
                min_idx = j
            # Сортировка по опыту (если должности и компании одинаковые)
            elif vacancies[min_idx].position == vacancies[j].position and vacancies[min_idx].company == vacancies[j].company and vacancies[min_idx].experience < vacancies[j].experience:
                min_idx = j
        vacancies[i], vacancies[min_idx] = vacancies[min_idx], vacancies[i]
    return vacancies

def stable_selection_sort(vacancies):
    """Сортировка выбором (устойчивая) по должности, затем по фирме, затем по опыту (в убывающем порядке).

    Args:
        vacancies (list): Список объектов Vacancy.

    Returns:
        list: Отсортированный список объектов Vacancy.
    """
    n = len(vacancies)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Сортировка по должности
            if vacancies[min_idx].position > vacancies[j].position:
                min_idx = j
            # Сортировка по компании (если должности одинаковые)
            elif vacancies[min_idx].position == vacancies[j].position and vacancies[min_idx].company > vacancies[j].company:
                min_idx = j
            # Сортировка по опыту (если должности и компании одинаковые)
            elif vacancies[min_idx].position == vacancies[j].position and vacancies[min_idx].company == vacancies[j].company and vacancies[min_idx].experience < vacancies[j].experience:
                min_idx = j
        # Если найден меньший элемент, меняем местами
        if min_idx != i:
            vacancies[i], vacancies[min_idx] = vacancies[min_idx], vacancies[i]
    return vacancies

def insertion_sort(vacancies):
    """Сортировка вставками по должности, затем по фирме, затем по опыту (в убывающем порядке).

    Args:
        vacancies (list): Список объектов Vacancy.

    Returns:
        list: Отсортированный список объектов Vacancy.
    """
    n = len(vacancies)
    for i in range(1, n):
        key = vacancies[i]
        j = i - 1
        # Сортировка по должности, компании и опыту
        while j >= 0 and (key.position < vacancies[j].position or (key.position == vacancies[j].position and key.company < vacancies[j].company) or (key.position == vacancies[j].position and key.company == vacancies[j].company and key.experience < vacancies[j].experience)):
            vacancies[j + 1] = vacancies[j]
            j -= 1
        vacancies[j + 1] = key
    return vacancies

def print_vacancies(vacancies):
    """Печатает информацию о вакансиях."""
    for vacancy in vacancies:
        print(vacancy)

# Считываем вакансии из CSV-файла
vacancies = read_vacancies('/Users/arseniy/Documents/GitHub/ITP/2 Семестр/vacancies.csv')  

# Сортируем вакансии разными алгоритмами
bubble_sorted = bubble_sort(vacancies.copy())
selection_sorted = selection_sort(vacancies.copy())
stable_selection_sorted = stable_selection_sort(vacancies.copy())
insertion_sorted = insertion_sort(vacancies.copy())

# Выводим результаты
print("Сортировка пузырьком:")
print_vacancies(bubble_sorted)
print("\nСортировка выбором:")
print_vacancies(selection_sorted)
print("\nСортировка выбором (устойчивая):")
print_vacancies(stable_selection_sorted)
print("\nСортировка вставками:")
print_vacancies(insertion_sorted)