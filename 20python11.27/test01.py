# P180 6.1
import random


def Ranpass():
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    L = list(s)
    T = 0
    print("生成的密码是:")
    while T < 10:
        pwd = ""
        for i in range(8):
            pwd += L[random.randint(0, len(L) - 1)]
        print("{}".format(pwd))
        T = T + 1
    print("输出结束")


Ranpass()
