input_file = "/Users/arseniy/Documents/GitHub/ITP/2 Семестр/input8.1.txt"

def find_positions(input_file):
    with open(input_file, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    print("Input data:", input_data)

    word_positions = {}
    for i, line in enumerate(input_data):
        words = line.split()
        for j, word in enumerate(words):
            if word not in word_positions:
                word_positions[word] = []
            word_positions[word].append(i + 1)
            word_positions[word].append(j + 1)

    print("Word positions:")
    for word, positions in word_positions.items():
        print(f"{word}: {positions}")

    return word_positions

#1. Определяется переменная `input_file`, содержащая путь к файлу `input8.1.txt`.
#   
#2. Объявляется функция `find_positions(input_file)` с аргументом `input_file`.
#
#3. Функция открывает файл `input_file` в режиме чтения (`'r'`) и связывает его с переменной `f` с помощью оператора `with open(input_file, 'r') as f:`.
#
#4. Читается содержимое файла `f` с помощью метода `readlines()`, каждая строка удаляется от возможных символов переноса строки с помощью `strip()`, и результат сохраняется в виде списка строк `input_data`.
#
#5. Выводится на экран `Input data:` и выводится список строк `input_data`.
#
#6. Создается пустой словарь `word_positions`, который будет хранить информацию о позициях слов.
#
#7. Проход по строкам файла осуществляется через `enumerate(input_data)`, где `i` - номер строки, `line` - содержимое строки.
#
#8. Каждая строка `line` разбивается на слова с помощью метода `split()` и результирующий список слов сохраняется в переменную `words`.
#
#9. Проход по словам в каждой строке осуществляется через `enumerate(words)`, где `j` - порядковый номер слова, `word` - само слово.
#
#10. Проверяется, если слово `word` не содержится в словаре `word_positions`, то создается новая запись со словом в словаре и списком позиций.
#
#11. Позиции слова `word` (номер строки `i+1` и номер слова в строке `j+1`) добавляются в список позиций этого слова в словаре `word_positions`.
#
#12. После обработки всех слов выводится `Word positions:`.
#
#13. Для каждого слова и его позиций в словаре `word_positions` выводится информация о слове и соответствующих позициях.
#
#14. В конце функция возвращает словарь `word_positions`, содержащий информацию о позициях слов в файле.