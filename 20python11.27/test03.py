# P180 6.5
import random


def Birthparadox():
    times = 50
    count = 0
    for i in range(times):
        lis = []
        for j in range(23):
            lis.append(random.randint(1, 365))
        items = set(lis)
        if len(items) != len(lis):
            count += 1
    print("至少两人生日相同的概率:{:.6f}%".format(count / times * 100))


Birthparadox()
