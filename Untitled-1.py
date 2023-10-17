#def count_ways(N):
#    count = 0
#    for length in range(2, N//2 + 1):
#        start = (N - length*(length-1)//2) // length
#        if start <= 0:
#            break
#        if start*(2*start + length - 1) == 2*N:
#            count += 1
#    return count
#
#N = 10000
#max_ways = 0
#for num in range(1000, N):
#    ways = count_ways(num)
#    if ways > max_ways:
#        max_ways = ways
#
#print(max_ways)
# cnt = 0
# for n in range(100_000, 1_000_000):
#     s = str(n)
#     sm1 = sum([int(x) for x in s[:3]])
#     sm2 = sum([int(x) for x in s[3:]])
#     if "666" in s and sm1 == sm2:
#         cnt += 1
#         # print(s)
# print(cnt)

# def check(a):
#     for x in range(2, a // 2 + 1):
#         if a % x == 0:
#             return False
#     return True

# print([7 ** x for x in ])
# import sys
# sys.set_int_max_str_digits(1000000000)
# for x in range(1, 1000000):
#     if str(7 ** int(x * str("9"))).count("9") == 1000:
#         print(7 ** x)
#         break

# for a in range(1, 40):
#     for b in range(1, 40):
#         for c in range(1, 40):
#             if ((a ** 2 + b ** 2 + c ** 2) == 989) and ((a + b)**2 + (b+c)**2 + (c+a)**2 == 2013):
#                 print(a, b, c)

# for a in range(1, 1000000):
#     s = str(a)
#     res = 1
#     for n in s:
#         res *= int(n)
#     if res == 6**6:
#         print(a)
#         break

print(2010 - )