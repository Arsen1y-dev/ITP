def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  #Проверяем, является ли символ буквой
            shift_amount = shift % 32   #Переводим сдвиг в диапазон [0, 32]
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('а') + shift_amount) % 32) + ord('а'))
            else:
                encrypted_char = chr(((ord(char) - ord('А') + shift_amount) % 32) + ord('А'))
        else:
            encrypted_char = char   #Если символ не является буквой, оставляем его без изменений
        encrypted_text += encrypted_char
    return encrypted_text

text_to_encrypt = "Скфрп- ржкп кй увоэч срсхнбтпэч бйэмрд стретвооктрдвпкб. Рп ргнвжвзф струфэо к српбфпэо укпфвмукуро, щфр жзнвзф зер рфнкщпэо дэгртро жнб пвщкпваыкч. Скфрп сржжзтикдвзф твйнкщпэз свтвжкеоэ стретвооктрдвпкб, дмнащвб ргьзмфпр-рткзпфктрдвппрз, стршзжхтпрз к цхпмшкрпвнюпрз стретвооктрдвпкз. Рп фвмиз коззф ъктрмкл усзмфт гкгнкрфзм, мрфртэз жзнваф зер яццзмфкдпэо жнб твйтвгрфмк дзг-сткнризпкл, впвнкйв жвппэч, овъкппрер ргхщзпкб к жтхекч ргнвуфзл."
shift = 2
encrypted_text = caesar_cipher(text_to_encrypt, shift)
print("Зашифрованный текст:", encrypted_text)


