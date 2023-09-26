## 1.2 Ветвление
#
#
#
#
## Плотность тела (1)
#
#
## Ввод данных
#V1 = int(input())
#m1 = int(input())
#V2 = int(input())
#m2 = int(input())
#
## Вычисляем плотности
#density1 = m1 / V1
#density2 = m2 / V2
#
## Сравниваем плотности и выводим результат
#if density1 > density2:
#    print(1)
#elif density2 > density1:
#    print(2)
#else:
#    print("=")
#
#
#
## Високосный год (2)
#
#
## Ввод года
#y = int(input())
#
## Проверка, является ли год високосным
#if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#    print(29)  # Год високосный, в феврале 29 дней
#else:
#    print(28)  # Год не високосный, в феврале 28 дней
#
#
#
## Вася и работа (3)
#
#
#n = int(input())
#
#if (n % 3 == 0) and (n % 10 == 3):
#    print('0')  
#elif n % 3 == 0:
#    print('1')  
#elif n % 10 == 3:
#    print('1')
#else:
#    print('0')
#
#
## Области. Задача 7 (4)
#
#
#x, y = map(float, input().split())
#
#if x >= 2:
#    print("Yes")
#elif 0.5 <= y <= 1.5:
#    print("Yes")
#else:
#    print("No")
#
#
#
#
# Улитка на координатной прямой (5)


#s = input().split()
#x1 = int(s[0])
#x2 = int(s[1])
#x3 = int(s[2])
#res = 0
#if abs(x1 - x2) > abs(x1 - x3):
#    res = res + abs(x1 - x3)
#    res = res + abs(x3 - x2)
#else:
#    res = res + abs(x1 - x2)
#    res = res + abs(x2 - x3)
#print(res)
#
#
#
## Бассейн (6)
#
#

# n = int(input()) 
# m = int(input()) 
# x = int(input()) 
# y = int(input()) 
# 
# len_short = min(n, m) 
# len_long = max(n, m) 
# 
# dist_to_short = min(x, len_short - x) 
# dist_to_long = min(y, len_long - y) 
# 
# print(min(dist_to_short, dist_to_long)) 

#
#
## Сундук с сокровищами (7)
#
#
# a = int(input()) 
# b = int(input()) 
# c = int(input()) 
# d = int(input()) ** 2 
# 
# diag1 = a ** 2 + b ** 2 
# diag2 = a ** 2 + c ** 2 
# diag3 = b ** 2 + c ** 2 
# 
# if diag1 <= d or diag2 <= d or diag3 <= d: 
#     print("Yes") 
# else: 
#     print("No") 
#
#
#
## Возраст (8)
#
#
#k = int(input())
#
# k = int(input()) 
# 
# if 10 <= (k % 100) <= 19: 
#     print(f"Мне {k} лет") 
# elif k % 10 == 1: 
#     print(f"Мне {k} год") 
# elif 2 <= (k % 10) <= 4: 
#     print(f"Мне {k} года") 
# else: 
#     print(f"Мне {k} лет")
