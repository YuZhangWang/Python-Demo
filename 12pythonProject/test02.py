# 汇率兑换程序
def transformation():
    while (True):
        tmp = eval(input("请输入需要转换的金额:"))
        tmp1 = input("该金额是美元(D)还是人民币(R)？")
        if tmp1 in {'D', 'd'}:
            R = tmp * 6
            print("转换后的金额为:%d￥" % R)
            break
        elif tmp1 in {'R', 'r'}:
            D = tmp / 6
            print("转换后的金额为:%d＄" % D)
            break
        else:
            print("ERROR INPUT!")
transformation()
