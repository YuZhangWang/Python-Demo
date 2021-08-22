import random;

'''
s = "PYTHON"
while s != "":
    for c in s:
        print(c, end="")
    s = s[:-1]

s = "PYTHON"
while s != "":
    for c in s:
        if c == "T":
            break
        print(c, end="")
    s = s[:-1]
'''
print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
print(random.uniform(1.1, 8.8))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
print(random.choice('python'))  # 从序列中随机选取一个元素
