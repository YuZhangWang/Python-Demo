'''
1)先来先服务（FCFS）算法：根据进程请求访问磁盘的先后次序进行调度。
算法的实现简单、公平；缺点：效率不高，相临两次请求可能会造成最内到最外的柱面寻道，使磁头反复移动，增加了服务时间，对机械也不利；
2)最短寻道时间优先（SSTF）算法：优先选择距当前磁头最近的访问请求进行服务，主要考虑寻道优先。
优点：改善了磁盘平均服务时间；缺点：造成某些访问请求长期等待得不到服务
3)扫描（SCAN）算法：当设备无访问请求时，磁头不动；当有访问请求时，磁头按一个方向移动，在移动过程中对遇到的访问请求进行服务，
然后判断该方向上是否还有访问请求，如果有则继续扫描；否则改变移动方向，并为经过的访问请求服务，如此反复。克服了最短寻道优先的缺点，
4)既考虑了距离，同时又考虑了方向；
循环扫描（C-SCAN）算法：总是从0号柱面开始向里扫描，按照各自所要访问的柱面位置的次序去选择访问者，移动臂到达最后一个柱面后，
立即带动读写磁头快速返回到最小的需要方面的柱面，返回时不为任何的等待访问者服务，返回后可再次进行扫描。
'''


def loaddata(fileName):  # 读取数据
    f = open(fileName)
    start = f.readline()  # 读入data文件的第一行作为起始磁道
    data = f.readline()  # 依次读入数据作为下一个被访问的磁道号
    return start, data


def loadnext(now, next):  # 输出下一个被访问的磁道号和移动距离
    length = abs(int(now) - int(next))  # 移动距离
    str_length = str(length)
    if len(next) == 3:
        if len(str_length) == 1:
            print("|         ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("        |")
        elif len(str_length) == 2:
            print("|         ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("       |")
        else:
            print("|         ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("      |")
    elif len(next) == 2:
        if len(str_length) == 1:
            print("|          ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("        |")
        elif len(str_length) == 2:
            print("|          ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("       |")
        else:
            print("|          ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("      |")
    elif len(next) == 1:
        if len(str_length) == 1:
            print("|           ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("        |")
        elif len(str_length) == 2:
            print("|           ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("       |")
        else:
            print("|           ", end="")
            print(next, end="")
            print("         |   ", end="")
            print("    ", end="")
            print(length, end="")
            print("      |")
    return length


def FCFS():
    l = 0
    start, data = loaddata('data')
    print("|--------------------------------------|")
    print("|  被访问的下一个磁道号  |     移动距离     |")
    print("|--------------------------------------|")
    for d in data.split():
        l += loadnext(start, d)  # 循环输出下一个磁道号和移动距离，并将寻道距离累加
        start = d  # 将刚访问的磁道作为下次访问的起始磁道
    n = len(data.split())
    print("|--------------------------------------|")
    print("| 先来先服务(FCFS)的平均寻道长度：%.1f      |" % (l / n))
    print("|--------------------------------------|")


def findnextindex(start, datas):  # SSTF算法
    length = []
    for data in datas:
        l = abs(int(start) - int(data))  # 计算磁道间要移动的距离
        length.append(l)  # 计算的将每个距离放入距离数组
    minIndex = length.index(min(length))  # 在数组中选出最小的距离在数组中位置
    return minIndex


def SSTF():
    l = 0
    start, data = loaddata('data')
    data2 = data.split().copy()
    n = len(data2)
    print("|--------------------------------------|")
    print("|  被访问的下一个磁道号  |     移动距离     |")
    print("|--------------------------------------|")
    for d in data.split():
        nextIndex = findnextindex(start, data2)  # 获取每次的最小寻道距离
        l += loadnext(start, data2[nextIndex])
        start = data2[nextIndex]
        data2.remove(data2[nextIndex])

    print("|--------------------------------------|")
    print("|最短寻道时间优先(SSTF)的平均寻道长度：%.1f  |" % (l / n))
    print("|--------------------------------------|")


def findnext1(now, data):  # SCAN
    biggerList = []
    smallerList = []
    for d in data:
        if int(d) > int(now):  # 判断初始磁道和下一磁道的大小关系
            biggerList.append(d)  # 如果下一磁道号更大则将其放入大数组中
    if (len(biggerList) == 0):  # 否则则开始寻找比初始磁道小的磁道号
        if len(data) != 0:
            for d2 in data:
                if int(d2) < int(now):
                    smallerList.append(d2)  # 将其加入小数组中
            return max(smallerList)
        else:
            return None
    return min(biggerList)


def SCAN():
    l = 0
    start, data = loaddata('data')
    data2 = data.split().copy()
    print("|--------------------------------------|")
    print("|  被访问的下一个磁道号  |     移动距离     |")
    print("|--------------------------------------|")
    n = len(data2)
    for d in data:
        next = findnext1(start, data2)  #
        if next == None:
            break
        l += loadnext(start, next)
        start = next
        data2.remove(next)
    print("|--------------------------------------|")
    print("|电梯调度算法(SCAN)平均寻道长度：%.1f       |" % (l / n))
    print("|--------------------------------------|")


def findnext2(now, data):  # CSCAN
    biggerList = []
    smallerList = []
    for d in data:
        if int(d) > int(now):
            biggerList.append(d)
    if (len(biggerList) == 0):
        if len(data) != 0:
            now = 0
            return (findnext2(now, data))
        else:
            return None
    return min(biggerList)


def CSCAN():
    l = 0
    start, data = loaddata('data')
    data2 = data.split().copy()
    n = len(data2)
    print("|--------------------------------------|")
    print("|  被访问的下一个磁道号  |     移动距离     |")
    print("|--------------------------------------|")
    for d in data:
        next = findnext2(start, data2)
        if next == None:
            break
        l += loadnext(start, next)
        start = next
        data2.remove(next)
    print("|--------------------------------------|")
    print("|循环扫描算法(CSCAN)平均寻道长度：%.1f      |" % (l / n))
    print("|--------------------------------------|")


def main():
    num4 = int(input("恢复原磁道(1、是；0、否)："))
    if num4 == 1:
        filename = 'data'
        with open(filename, 'w') as f:
            first = "53"
            second = "98 138 37 122 14 124 65 67"
            f.write(first)
            f.write("\n")
            f.write(second)
    else:
        print("")
    start, data = loaddata('data')
    print("|------------磁盘调度算法程序-------------|")
    print("|------1、先来先服务      (FCFS )算法-----|")
    print("|------2、最短寻道时间优先 (SSTF )算法-----|")
    print("|------3、电梯调度        (SCAN )算法-----|")
    print("|------4、循环扫描算法     (CSCAN)算法-----|")
    print("|---------------------------------------|")
    print("初始磁道为:" + start + data)
    num = int(input("请选择要使用的调度算法(1~4):"))
    if num == 1:
        FCFS()
    elif num == 2:
        SSTF()
    elif num == 3:
        SCAN()
    elif num == 4:
        CSCAN()
    else:
        num1 = int(input("您没有做出选择，是否需要指定访问的磁道？(1:是 0:否)"))
        if num1 == 1:
            # 53
            # 98 138 37 122 14 124 65 67
            print("原磁道顺序为:53 \n" + "98 138 37 122 14 124 65 67")
            filename = 'data'
            with open(filename, 'w') as f:
                first = int(input("请输入初始访问磁道："))
                second = input("请输入被访问的下一个磁道号序列(用空格分开)：")
                f.write(str(first))
                f.write("\n")
                f.write(str(second))

        else:
            num3 = int(input("是否选择关闭程序？(1:是 0:否)"))
            if num3 == 1:
                print("程序结束！谢谢使用。")
                exit()
            elif num3 == 0:
                main()
            else:
                print("选择错误！")
                main()
    num2 = int(input("是否继续选择？(1:是 0:否,关闭程序)"))
    if num2 == 1:
        main()
    elif num2 == 0:
        print("程序结束！谢谢使用。")
        exit()
    else:
        print("选择错误！")
        main()


if __name__ == "__main__":
    main()
