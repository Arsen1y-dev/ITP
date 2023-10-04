#def encrypt_message(message, offset):
#    encrypted_message = "Тёплое место, но улицы ждут Отпечатков наших ног Звёздная пыль на сапогах Мягкое кресло, клетчатый плед Не нажатый вовремя курок Солнечный день в ослепительных снах Группа крови на рукаве Мой порядковый номер на рукаве Пожелай мне удачи в бою, пожелай мне Не остаться в этой траве Не остаться в этой траве Пожелай мне удачи, пожелай мне удачи И есть чем платить, но я не хочу Победы любой ценой Я никому не хочу ставить ногу на грудь Я хотел бы остаться с тобой Просто остаться с тобой Но высокая в небе звезда Зовёт меня в путь Группа крови на рукаве Мой порядковый номер на рукаве Пожелай мне удачи в бою, пожелай мне Не остаться в этой траве Не остаться в этой травеПожелай мне удачи, пожелай мне удачи"
#    
#    for byte in message:
#        # Считываем сообщение побайтово и добавляем смещение
#        encrypted_byte = byte + offset
#        
#        # Преобразуем байт в шестнадцатеричный код и удаляем префикс "0x"
#        hex_code = hex(encrypted_byte)[2:]
#        
#        # Добавляем шестнадцатеричный код к зашифрованному сообщению
#        encrypted_message += hex_code
#        
#    # Переворачиваем строку задом наперед
#    encrypted_message = encrypted_message[::-1]
#    
#    return encrypted_message
#
## Пример использования
#message = b"Hello, world!"  # Сообщение в байтах
#offset = 8  # Смещение
#encrypted_message = encrypt_message(message, offset)
#print("Зашифрованное сообщение:", encrypted_message)


def encrypt_message(input_file, output_file, offset):
    try:
        # Открываем файл для чтения в режиме "rb"
        with open(input_file, "rb") as file:
            # Считываем все байты из файла
            byte_data = file.read()

            # Преобразуем каждый байт в шестнадцатеричное представление
            hex_data = ''.join([hex(byte)[2:].zfill(2) for byte in byte_data])

            # Добавляем смещение к каждому шестнадцатеричному символу
            shifted_hex_data = ''.join([hex((int(char, 16) + offset) % 256)[2:].zfill(2) for char in hex_data])

            # Переводим полученные данные обратно в байты
            shifted_byte_data = bytes.fromhex(shifted_hex_data)

            # Переворачиваем строку задом наперед
            reversed_data = shifted_byte_data[::-1]

            # Открываем файл для записи в режиме "wb"
            with open(output_file, "wb") as output:
                output.write(reversed_data)

            print("Сообщение успешно зашифровано и записано в файл", output_file)

    except Exception as e:
        print("Произошла ошибка:", str(e))

input_file = "qws.txt"  # Замените на имя вашего входного файла
output_file = "encrypted_message8.bin"  # Замените на имя файла для сохранения зашифрованного сообщения
offset = 5  # Замените на ваше собственное смещение
encrypt_message(input_file, output_file, offset)


