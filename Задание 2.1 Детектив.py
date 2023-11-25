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














def scene1():
    print("Вы находитесь в гостиной.")
    print("Доступные действия:")
    print("1. Осмотреть тело")
    print("2. Поговорить со свидетелями")
    print("3. Осмотреть шкаф")
    print("4. Перейти в другую комнату")
    print("5. Выйти на улицу")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        examine_body()
    elif choice == "2":
        talk_to_witnesses()
    elif choice == "3":
        examine_closet()
    elif choice == "4":
        scene2()
    elif choice == "5":
        scene3()
    else:
        print("Неверный выбор. Попробуйте еще раз.")
        scene1()

def examine_body():
    print("Осмотр тела...")
    # Логика осмотра тела

def talk_to_witnesses():
    print("Разговор со свидетелями...")
    # Логика разговора со свидетелями

def examine_closet():
    print("Осмотр шкафа...")
    # Логика осмотра шкафа
    print("Вы нашли фонарик!")
    # Добавить фонарик в инвентарь игрока

def scene2():
    print("Вы находитесь на улице.")
    print("Доступные действия:")
    print("1. Осмотреть подвал")
    print("2. Вернуться в дом")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        examine_basement()
    elif choice == "2":
        scene1()
    else:
        print("Неверный выбор. Попробуйте еще раз.")
        scene2()

def examine_basement():
    print("Осмотр подвала...")
    # Логика осмотра подвала (требуется фонарик)

def scene3():
    print("Вы вернулись в гостиную.")
    print("Доступные действия:")
    print("1. Сравнить отпечатки с отпечатками свидетелей")
    print("2. Обвинить кого-то из свидетелей")
    print("3. Продолжить расследование")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        compare_fingerprints()
    elif choice == "2":
        accuse()
    elif choice == "3":
        continue_investigation()
    else:
        print("Неверный выбор. Попробуйте еще раз.")
        scene3()

def compare_fingerprints():
    print("Сравнение отпечатков...")
    # Логика сравнения отпечатков

def accuse():
    print("Обвинение...")
    # Логика обвинения

def continue_investigation():
    print("Продолжение расследования...")
    # Логика продолжения расследования

# Запуск игры
scene1()
