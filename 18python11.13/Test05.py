# P121 4.7
while 1:
    try:
        TempStr = input("请输入带有符号的温度值:")
        if TempStr[-1] in ['F', 'f']:
            C = (eval(TempStr[0:-1]) - 32) / 1.8
            print("转换后的温度是:{:.2f}C".format(C))
            break
        elif TempStr[-1] in ['C', 'c']:
            F = 1.8 * eval(TempStr[0:-1]) + 32
            print("转换后的温度是:{:.2f}F".format(F))
            break
        else:
            print("输入的内容错误!")
    except:
        print("输入的格式错误!")