import itertools

encrypted_message = "ラネイヤナム ラシテノ ヤヒキノハヒサラ ヤヒミ イノアタイ, ハイムラヒン キハム ハヨムミナ キムハムヤヤムニタ カアタワシヘミムヤノン."

# Разрешенные символы (подставьте здесь символы, которые вы ожидаете в сообщении)
allowed_characters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

# Функция для проверки, является ли текст реальным русским текстом
def is_valid_russian_text(text):
    # Преобразуем текст в нижний регистр и разбиваем на слова
    words = text.lower().split()
    
    # Пример словаря с русскими словами (замените его на свой словарь)
    russian_dictionary = {"шифр", "код", "привет", "я", "ты", "он", "мы", "нет", "основа", "кот", "карлик"}
    
    # Проверяем, есть ли хотя бы одно слово из текста в словаре
    for word in words:
        if word in russian_dictionary:
            return True
    
    return False

# Перебор всех возможных комбинаций символов и проверка на соответствие реальному русскому тексту
def decrypt_message(message, allowed_chars):
    for i in range(1, len(allowed_chars) + 1):
        for combination in itertools.product(allowed_chars, repeat=i):
            candidate = ''.join(combination)
            decrypted = message
            for original_char, replacement in zip(allowed_characters, candidate):
                decrypted = decrypted.replace(original_char, replacement)
            if is_valid_russian_text(decrypted):
                return decrypted

# Вызываем функцию для расшифровки сообщения
decrypted_result = decrypt_message(encrypted_message, allowed_characters)
print(decrypted_result)
