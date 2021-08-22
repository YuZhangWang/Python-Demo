# 随机开柜码
import random


def RandomPassword():
    seed = int(input("请输入一个随机数种子n(n为整数):"))
    random.seed(seed)
    password = random.choice('ABCDEFGHIJ0123456789')
    for i in range(5):
        password = "{}{}".format(password, random.choice('ABCDEFGHIJ0123456789'))
    print(password)


RandomPassword()
