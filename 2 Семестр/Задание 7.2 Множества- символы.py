number_of_strings = int(input("Enter the number of strings: "))

for _ in range(number_of_strings):
    string = input("Enter a string: ")
    
    letters_from_string = set()
    
    for char in string:
        if char.isalpha():
            if char.lower() in letters_from_string or char.upper() in letters_from_string:
                letters_from_string.add(char.lower())
                letters_from_string.add(char.upper())
    
    result = ''.join(sorted(letters_from_string))
    print(result)
