numbers = input().split()

for number in numbers:
    unique_digits = set(number)
    result = []
    for digit in unique_digits:
        if number.count(digit) % 2 == 0:
            result.append(digit)
    print(''.join(result))   
    