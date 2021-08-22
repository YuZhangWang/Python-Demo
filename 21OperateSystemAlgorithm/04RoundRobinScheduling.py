import random


def createP(randnum):
    """
    创建字典，根据输入的进程数进行创建进程字典，时间为随机1-9s之间
    """
    p_dict = {}
    # 获取一个a-z的列表
    alphabet_list = list(map(chr, range(ord('a'), ord('z') + 1)))

    for i in range(0, randnum):
        # 默认进程名为a-z顺序排序
        p_dict[alphabet_list[i]] = random.randint(1, 9)
    return p_dict


def lunzhuanP(p_dict, randnum):
    """
    开始轮转
    """
    print("进程名称" + " " + "每个进程需要工作的时间")
    p_time = {}
    p_list = [[-1 for i in range(4)] for j in range(randnum + 1)]
    # 添加输出头
    p_list[0][0] = "Name"
    p_list[0][1] = "run"
    p_list[0][2] = "req"
    p_list[0][3] = "status"
    z = 1
    for name, time in p_dict.items():
        # 将进程初始化设置初始值
        p_list[z][0] = name
        p_list[z][1] = 0
        p_list[z][2] = time
        p_list[z][3] = "R"
        p_time[name] = 0
        z += 1

    # 将随机生产的进程名和所需时间打印出来
    for name, time in p_dict.items():
        print("\t" + name + "\t\t\t", time)

    # 判断条件
    j = 1
    # 代表CPU时刻
    t = 1
    while True:
        if len(p_list) == 1:
            print("进程执行完毕")
            for name, time in p_time.items():
                print("进程%s的执行周期为:%s" % (name, time))
            break

        # 判断是否有进程执行完毕
        for y in range(1, len(p_list) - 1):
            if p_list[y][3] == "E":
                del p_list[y]

        # 轮转到，进行加1操作
        if len(p_list) - 1 >= j:
            if p_list[j][1] + 1 <= p_list[j][2]:
                p_list[j][1] += 1
                if p_list[j][1] == p_list[j][2]:
                    p_list[j][3] = "E"
            else:
                del p_list[j]
                continue
        else:
            j = j - len(p_list) + 1
            continue

        print("cpu时刻:", t)
        print("正在执行的进程:", p_list[j][0])
        # 对应进程名的操作进行+1，代表运行了1个周期
        p_time[p_list[j][0]] += 1
        j += 1
        t += 1
        for i in range(len(p_list)):
            print(p_list[i])


def main():
    while True:
        randnum = input("请输入进程数:")
        if randnum.isdigit():
            randnum = int(randnum)
            p_dict = createP(randnum)
            lunzhuanP(p_dict, randnum)

        else:
            print("输入的不是有效数字")


if __name__ == "__main__":
    main()
