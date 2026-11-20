# 输入列表
lstA = list(map(int, input("请输入列表A，空格分隔：").split()))
lstB = list(map(int, input("请输入列表B，空格分隔：").split()))
# 取短的那个的长度
n = min(len(lstA), len(lstB))
d = {lstA[i]: lstB[i] for i in range(n)}
print(d)

lst = list(map(int, input("输入整数列表，空格分隔：").split()))
new_lst = sorted(lst, reverse=True)
print(new_lst)

lst = list(map(int, input("输入整数列表，空格分隔：").split()))
res = 1
for num in lst:
    res *= num
print("连乘结果：", res)

p1 = list(map(int, input("输入第一个点坐标：").split()))
p2 = list(map(int, input("输入第二个点坐标：").split()))
dis = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
print("曼哈顿距离 =", dis)
