## Задание 1.1 Билеты в кино
#
#
#cinema_name = input("Введите название кинотеатра: ")
#movie_name = input("Введите название фильма: ")
#
#seances = ["10:00", "15:30", "20:15"]
#
#print("Выберите сеанс:")
#for i, seance in enumerate(seances, 1):
#    print(f"{i}. {seance}")
#
## Запрос выбора сеанса у пользователя
#try:
#    choice = int(input("Введите номер сеанса (1, 2 или 3): "))
#    if 1 <= choice <= 3:
#        chosen_seance = seances[choice - 1]
#        print(f"Вы успешно забронировали билеты в кинотеатр “{cinema_name}” на фильм “{movie_name}”.")
#        print(f"Сеанс начинается в {chosen_seance}. Приятного просмотра!")
#    else:
#        print("Ошибка: Вы выбрали несуществующий сеанс.")
#except ValueError:
#    print("Ошибка: Введите номер сеанса числом (1, 2 или 3).")
#
#
#
## Задание 1.2 Калькулятор процентов
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


# Задание 1.3* Генератор сказок


# Запрос информации о сказке
hero_name = input("Как зовут героя? ")
villain_name = input("Кто его противник? ")
kingdom_name = input("Название места действия? ")
conflict_reason = input("Причина конфликта? ")
hero_weapon = input("Оружие героя? ")
villain_ability = input("Способность злодея? ")
years = input("Сколько лет герою? ")

# Вывод текста сказки с подстановками
print(f"Жил-был в королевстве {kingdom_name} герой {hero_name}. Было ему {years} лет.")
print(f"Однажды на королевство напал злой {villain_name}.")
print(f"Причина конфликта была следующей: {conflict_reason}.")
print(f"Герой {hero_name} вооружен {hero_weapon}, а злодей {villain_name} обладает ужасной способностью: {villain_ability}.")
print(f"День бились, другой бились, наконец {hero_name} одолел врага.")
print(f"Вернулся домой, а {hero_name} забыл {hero_weapon} в лесу.")
print(f"Тут и сказочке конец, а кто слушал — молодец!")
