nums = [int(x.strip("-")) for x in input().split()]
res = {}
for num in nums:
    s_num = str(num)
    cur_res = set(s_num)
    for dig in s_num:
        cur_res.add(dig) if dig not in cur_res else cur_res.remove(dig)
    res[num] = cur_res

print(res)