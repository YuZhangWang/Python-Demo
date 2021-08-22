# 华氏度和摄氏度转换器
def transformation():
    while (True):
        tmp = eval(input("请输入需要转换的温度:"))
        tmp1 = input("该温度是华氏度(F)还是摄氏度(C)？")
        if tmp1 in {'F', 'f'}:
            C = (tmp - 32) / 1.8
            print("转换后的温度为:%dC"%C)
            break
        elif tmp1 in {'C', 'c'}:
            F = tmp * 1.8 + 32
            print("转换后的温度为:%dF"%F)
            break
        else:
            print("ERROR INPUT!")
transformation()