# Задание 1.1 Билеты в кино
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
