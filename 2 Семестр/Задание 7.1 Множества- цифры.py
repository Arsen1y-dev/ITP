nums = [int(x.strip("-")) for x in input().split()]
res = {}
for num in nums:
    s_num = str(num)
    cur_res = set(s_num)
    for dig in s_num:
        cur_res.add(dig) if dig not in cur_res else cur_res.remove(dig)
    res[num] = set(int(x) for x in cur_res)

print("\n".join(": ".join((str(key),
                           str(value if len(value) > 0 else "Таких цифр нет"))) for key, value in res.items()))