
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
word = input()  # Вводим слово

# Используем срез [::-1], чтобы получить обратное слово, затем выводим каждую букву в отдельной строке
for letter in word[::-1]:
    print(letter)
