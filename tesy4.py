# 输入，用逗号分隔元素
a = set(map(int, input("输入第一个集合，元素用逗号隔开：").split(',')))
b = set(map(int, input("输入第二个集合，元素用逗号隔开：").split(',')))
print("交集：", a & b)
print("并集：", a | b)
print("差集a-b：", a - b)
print("差集b-a：", b - a)

