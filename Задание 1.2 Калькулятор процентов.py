# Задание 1.2 Калькулятор процентов
#
#
## Запрос ввода числа
#try:
#    number = float(input("Введите число: "))
#except ValueError:
#    print("Ошибка: Введите корректное число.")
#else:
#    # Вывод вариантов действий
#    print("Выберите действие:")
#    print("1. Найти процент от введённого числа.")
#    print("2. Увеличить число на процент.")
#    print("3. Уменьшить число на процент.")
#    
#    # Запрос выбора действия у пользователя
#    try:
#        choice = int(input("Введите номер действия (1, 2 или 3): "))
#        if choice in (1, 2, 3):
#            # Запрос ввода процента
#            try:
#                percent = float(input("Введите процент (неотрицательное значение): "))
#                if percent >= 0:
#                    if choice == 1:
#                        result = number * (percent / 100)
#                        print(f"{percent}% от числа {number} равно {result}.")
#                    elif choice == 2:
#                        result = number * (1 + percent / 100)
#                        print(f"{number} увеличено на {percent}% равно {result}.")
#                    else:
#                        result = number * (1 - percent / 100)
#                        print(f"{number} уменьшено на {percent}% равно {result}.")
#                else:
#                    print("Ошибка: Введите неотрицательное значение процента.")
#            except ValueError:
#                print("Ошибка: Введите корректное значение процента.")
#        else:
#            print("Ошибка: Вы выбрали неверное действие.")
#    except ValueError:
#        print("Ошибка: Введите номер действия числом (1, 2 или 3).")
