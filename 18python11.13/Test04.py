# P121 4.6
import random as r


def SheepCarDoor():
    while (1):
        try:
            total = int(input("请输入需要进行的实验次数:\n"))
            # 不换的获胜次数
            win1 = 0
            # 换的获胜次数
            win2 = 0

            for i in range(total):
                # 模拟选择过程
                man = r.randint(1, 3)
                car = r.randint(1, 3)
                '''
                结果:一开始选择为车门，win1不换获胜次数+1
                      否则一开始选择为羊门，win2换获胜次数+1
                '''
                if man == car:
                    win1 += 1
                else:
                    win2 += 1

            print("在{}次实验中：".format(total))
            print("若不更改门，获胜概率为{:.3}%.".format((win1 / total) * 100))
            print("若更改门，获胜概率为{:.3}%.".format((win2 / total) * 100))
            break

        except:
            print("请输入一个整数!")


SheepCarDoor()
