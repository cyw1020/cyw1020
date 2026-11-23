from functools import reduce

# 示例：输入集合列表
set_list = [{1, 2, 3}, {3, 4, 5}, {5, 6}]
union_set = reduce(lambda s1, s2: s1 | s2, set_list)
print("并集：", union_set)

a1 = int(input("请输入首项："))
q = int(input("请输入公比："))
n = int(input("请输入n："))

Sn = a1 * (1 - q ** n) / (1 - q)
Sn = int(Sn)   # 题目要求关键步骤使用int()
print("等比数列前n项和 =", Sn)

s = input("请输入字符串：")
count_dict = {}
for c in s:
    count_dict[c] = count_dict.get(c, 0) + 1

# 找次数最大
max_key = max(count_dict, key=count_dict.get)
print(f"出现最多的字符：{max_key}，次数：{count_dict[max_key]}")

s = input("请输入任意长字符串：")
freq = {}
for ch in s:
    if ch.isalnum():   # 判断是否字母/数字
        freq[ch] = freq.get(ch, 0) + 1
print("频次字典：", freq)

