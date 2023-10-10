# Задание 2.1* Детектив


import time

def intro():
    print("Добро пожаловать в детективную историю!")
    print("Вы - детектив, расследующий загадочное убийство.")
    print("Вы находитесь в комнате с трупом. Что вы хотите сделать?")
    time.sleep(1)
    print("1. Поговорить со свидетелем.")
    print("2. Заглянуть в шкаф.")
    print("3. Перейти в другую комнату.")
    print("4. Выйти на улицу.")
    choice = input("Выберите действие (1/2/3/4): ")
    if choice == "1":
        interrogate_witness()
    elif choice == "2":
        check_closet()
    elif choice == "3":
        enter_another_room()
    elif choice == "4":
        go_outside()
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
        intro()

def interrogate_witness():
    print("Вы решили поговорить со свидетелем.")
    print("Свидетель говорит, что видел нечто странное ночью.")
    time.sleep(1)
    print("1. Спросить, что именно он видел.")
    print("2. Спросить, есть ли у него какие-либо улики.")
    print("3. Вернуться назад.")
    choice = input("Выберите действие (1/2/3): ")
    if choice == "1":
        print("Свидетель рассказывает вам о темной фигуре, убегающей с места преступления.")
        time.sleep(1)
        interrogate_witness()
    elif choice == "2":
        print("Свидетель говорит, что нашел нож возле трупа.")
        time.sleep(1)
        interrogate_witness()
    elif choice == "3":
        intro()
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
        interrogate_witness()

def check_closet():
    print("Вы заглянули в шкаф и нашли фонарик.")
    time.sleep(1)
    intro()

def enter_another_room():
    print("Вы перешли в другую комнату, но там ничего нет.")
    time.sleep(1)
    intro()

def go_outside():
    print("Вы вышли на улицу и видите темное небо.")
    print("1. Осмотреться вокруг.")
    print("2. Вернуться назад.")
    choice = input("Выберите действие (1/2): ")
    if choice == "1":
        print("Вы замечаете следы, ведущие в лес.")
        time.sleep(1)
        investigate_forest()
    elif choice == "2":
        intro()
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
        go_outside()

def investigate_forest():
    print("Вы идете в лес, следуя за следами.")
    print("1. Пойти дальше вглубь леса.")
    print("2. Вернуться на улицу.")
    choice = input("Выберите действие (1/2): ")
    if choice == "1":
        print("Вы находите заброшенную хижину и внутри обнаруживаете улику.")
        time.sleep(1)
        accuse_suspects()
    elif choice == "2":
        go_outside()
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
        investigate_forest()

def accuse_suspects():
    print("У вас есть несколько подозреваемых:")
    print("1. Мистер А")
    print("2. Миссис Б")
    print("3. Доктор В")
    choice = input("Кого вы хотите обвинить? (1/2/3): ")
    if choice == "1":
        print("Вы обвинили Мистера А, и это был верный ответ! Вы разгадали дело!")
    elif choice == "2" or choice == "3":
        print("Вы обвинили неверного человека. Дело остается нераскрытым.")
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
        accuse_suspects()

# Начать игру с ввода
intro()
