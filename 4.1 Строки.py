
##4.1 Строки
#
#
#
#
##Добавь звёзды!
#
#
#word = input()  
#stars = '*' * len(word)  
#result = stars + word + stars  
#print(result)
#
#
#
##Слово в столбик в обратном порядке
#
#
#word = input()  # Вводим слово
#
## Используем срез [::-1], чтобы получить обратное слово, затем выводим каждую букву в отдельной строке
#for letter in word[::-1]:
#    print(letter)
#
#
#
## Буквы на четных местах в обратном порядке
#
#
#s1 = input()
#s2 = s1[1::2]
#reversed_str = ''.join(reversed(s2))
#print(reversed_str)
#
#
#
## Строки. Задача 19
#
#
#def is_symmetric(s):
#    return s == s[::-1]
#
#s = input()
#
#if is_symmetric(s):
#    print(1)
#else:
#    print(0)
#
#
#
## Строки. Задача 3
#
#
#s = input()
#
#
#length = len(s)
#
#
#if length % 2 == 0:
#    middle = length // 2
#    result = s[:middle - 1] + s[middle + 1:]
#else:
#    middle = length // 2
#    result = s[:middle] + s[middle + 1:]
#
#print(result)
#
#
#
## Сумма цифр
#
#
s = input

