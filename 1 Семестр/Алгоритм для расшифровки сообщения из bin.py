def decrypt_message(input_file, output_file, offset):
    try:
        # Открываем файл для чтения в режиме "rb"
        with open(input_file, "rb") as file:
            # Считываем зашифрованные байты из файла
            byte_data = file.read()

            # Декодируем каждый байт, убирая смещение
            decrypted_byte_data = bytes([(byte - offset) % 256 for byte in byte_data])

            # Открываем файл для записи расшифрованного текста в текстовом формате
            with open(output_file, "w") as output:
                output.write(decrypted_byte_data.decode('utf-8'))

            print("Сообщение успешно расшифровано и записано в файл", output_file)

    except Exception as e:
        print("Произошла ошибка:", str(e))

# Пример использования
input_file = "encrypted_message8.bin"  # Замените на имя вашего зашифрованного файла
output_file = "decrypted_message7.txt"  # Замените на имя файла для сохранения расшифрованного текста
offset = 5  # Замените на то же смещение, которое использовалось при шифровании
decrypt_message(input_file, output_file, offset)