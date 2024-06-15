"""
С помощью быстрой сортировки (qsort), пирамидальной сортировки (heapsort), сортировки слиянием (mergesort) 
и встроенной сортировки Питона (функции sorted или метода списков sort) — расположить набор чисел в порядке убывания суммы цифр чисел
"""

def partition(arr, low, high, key):
    """Разделяет массив вокруг опорного элемента для быстрой сортировки."""
    pivot = key(arr[high])  # Выбор опорного элемента
    i = low - 1  # Индекс для меньшего элемента
    for j in range(low, high):
        # Если текущий элемент больше или равен опорному,
        # меняем местами с элементом после раздела
        if key(arr[j]) >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Меняем местами опорный элемент
    return i + 1  # Возвращаем индекс опорного элемента

def quick_sort(arr, low, high, key=lambda x: x):
    """Быстрая сортировка."""
    if low < high:
        pi = partition(arr, low, high, key)  # Разделяем массив
        quick_sort(arr, low, pi - 1, key)  # Рекурсивно сортируем левую часть
        quick_sort(arr, pi + 1, high, key)  # Рекурсивно сортируем правую часть
    return arr

def pushdown(arr, n, i, key):
    """Восстанавливает свойство кучи после удаления или изменения элемента."""
    largest = i  # Предполагаем, что корень является наибольшим
    left = 2 * i + 1  # Индекс левого ребенка
    right = 2 * i + 2  # Индекс правого ребенка

    # Сравниваем корень с его детьми
    if left < n and key(arr[left]) > key(arr[largest]):
        largest = left
    if right < n and key(arr[right]) > key(arr[largest]):
        largest = right
    # Если наибольшим элементом является не корень, меняем местами
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        pushdown(arr, n, largest, key)  # Рекурсивно восстанавливаем кучу

def heap_sort(arr, key=lambda x: x):
    """Пирамидальная сортировка."""
    n = len(arr)
    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        pushdown(arr, n, i, key)
    # Сортировка кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Меняем местами корень и последний элемент
        pushdown(arr, i, 0, key)  # Восстанавливаем кучу
    return arr[::-1]  # Возвращаем отсортированный массив в обратном порядке

def merge(arr, left, mid, right, key):
    """Слияние двух отсортированных подмассивов."""
    n1 = mid - left + 1
    n2 = right - mid
    L = [arr[left + i] for i in range(n1)]  # Левый подмассив
    R = [arr[mid + 1 + j] for j in range(n2)]  # Правый подмассив

    i = j = 0
    k = left  # Индекс для слияния

    while i < n1 and j < n2:
        if key(L[i]) >= key(R[j]):  # Сравниваем элементы из подмассивов
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:  # Копируем оставшиеся элементы из левого подмассива
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:  # Копируем оставшиеся элементы из правого подмассива
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right, key=lambda x: x):
    """Сортировка слиянием."""
    if left < right:
        mid = (left + right) // 2  # Находим середину массива
        merge_sort(arr, left, mid, key)  # Рекурсивно сортируем левую часть
        merge_sort(arr, mid + 1, right, key)  # Рекурсивно сортируем правую часть
        merge(arr, left, mid, right, key)  # Сливаем отсортированные подмассивы
    return arr

def sort_numbers(data):
    """Сортирует список чисел по убыванию суммы цифр."""
    quick_sorted = quick_sort(data.copy(), 0, len(data) - 1, key=lambda x: sum(map(int, str(abs(x)))))
    heap_sorted = heap_sort(data.copy(), key=lambda x: sum(map(int, str(abs(x)))))
    merge_sorted = merge_sort(data.copy(), 0, len(data) - 1, key=lambda x: sum(map(int, str(abs(x)))))
    python_sorted = sorted(data, key=lambda x: sum(map(int, str(abs(x)))), reverse=True)

    return quick_sorted, heap_sorted, merge_sorted, python_sorted

# Получение списка чисел от пользователя
data = list(map(int, input('Введите числа через пробел: ').split()))

sorted_lists = sort_numbers(data)

print("Результаты сортировки по убыванию суммы цифр чисел:")
print(f"Быстрая сортировка: {sorted_lists[0]}")
print(f"Пирамидальная сортировка: {sorted_lists[1]}")
print(f"Сортировка слиянием: {sorted_lists[2]}")
print(f"Встроенная сортировка: {sorted_lists[3]}")


"""
Тесты

Входные данные: 12 123 34 45 6 789
Сумма цифр: [3, 6, 7, 9, 6, 24]
Ожидаемый результат:
Быстрая сортировка: [789, 123, 45, 34, 12, 6]
Пирамидальная сортировка: [789, 123, 45, 34, 12, 6]
Сортировка слиянием: [789, 123, 45, 34, 12, 6]
Встроенная сортировка: [789, 123, 45, 34, 12, 6]

Входные данные: 5 50 500 5000
Сумма цифр: [5, 5, 5, 5]
Ожидаемый результат:
Быстрая сортировка: [5, 50, 500, 5000]
Пирамидальная сортировка: [5, 50, 500, 5000]
Сортировка слиянием: [5, 50, 500, 5000]
Встроенная сортировка: [5, 50, 500, 5000]

Входные данные: 91 82 73 64 55
Сумма цифр: [10, 10, 10, 10, 10]
Ожидаемый результат:
Быстрая сортировка: [91, 82, 73, 64, 55]
Пирамидальная сортировка: [91, 82, 73, 64, 55]
Сортировка слиянием: [91, 82, 73, 64, 55]
Встроенная сортировка: [91, 82, 73, 64, 55]
"""