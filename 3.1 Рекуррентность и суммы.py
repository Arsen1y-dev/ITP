## 3.1 Рекуррентность и суммы
#
#
#
#
## Числа Фибоначчи
#
#
#def fibonacci(k):
#    if k == 1 or k == 2:
#        return 1
#    else:
#        return fibonacci(k - 1) + fibonacci(k - 2)
#
#k = int(input())
#result = fibonacci(k)
#print(result)
#
#
#
## Винни Пух
#
#
#def winnie_puh_birthday(n):
#    if n == 1 or n == 2:
#        return 0.1
#    
#    honey = [0.1] * (n + 1)
#    
#    for i in range(3, n + 1):
#        honey[i] = honey[i - 1] + honey[i - 2]
#    
#    return honey[n]
#
#n = int(input())
#result = winnie_puh_birthday(n)
#print("{:.1f}".format(result))
#
#
#

