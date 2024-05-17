n = int(input())
for _ in range(n):
    a, s, b = input().split("%")
    s = s[:int(a) - len(s) + 1]
    s = [s[i] for i in range(len(s) - 1, -1, -3)][:int(b)]
    print("".join(s[::-1]))