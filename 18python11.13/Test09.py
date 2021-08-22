# 数列求和
def SummationOfSequence():
    while 1:
        try:
            n = int(input())
            sum = 0
            if (n % 2 != 0):
                for odd in range(1, n + 1, 2):
                    sum += (1 / odd)
            else:
                for even in range(2, n + 1, 2):
                    sum += + (1 / even)
            print("{:.2f}".format(sum))
            break
        except:
            print("请输入一个自然数!")


SummationOfSequence()
