# P121 4.4
import random


def ForecastFigures():
    Presupposition = random.randint(0, 100)
    n = 1
    while (1):
        guess = int(input("请通过键盘输入一个数来猜测预设的数:\n"))
        if (guess > Presupposition):
            print("遗憾，太大了")
            n += 1
            continue
        elif (guess < Presupposition):
            print("遗憾，太小了")
            n += 1
            continue
        else:
            print("预测{}次,你猜中了!".format(n))
            break


ForecastFigures()
