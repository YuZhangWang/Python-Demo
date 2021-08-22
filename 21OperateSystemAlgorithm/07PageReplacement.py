class page:
    def __init__(self, num, time):
        # 记录页面号
        self.num = num
        # 记录调入内存时间
        self.time = time


class main:
    # 初始化内存单元，缓冲区
    def __init__(self, M=4, N=20, a=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]):
        # 以上设定了默认值
        self.queue = []  # 记录调入队列
        self.k = -1  # 每载入一次加一 即缺页次数
        self.flag = -1  # 标记内存4个空
        self.a = a  # 需要排序的页面列表
        self.M = M  # 缓冲区的大小
        self.N = N  # 需要排序的页面列表的长度
        # 初始化内存单元
        self.b = [page(-1, self.M - i - 1) for i in range(0, self.M)]
        # 初始化内存当前状态，缓冲区 初始化页号全为-1
        self.c = [[-1 for i in range(0, self.N)] for j in range(0, self.M)]
        self.process()

    # 打印图表用
    def print_string(self):
        str = '---+'
        print('|', end='')
        for i in range(0, self.N - 1):
            print(str, end='')
        print("---|")

    # 取得在内存中停留最久的页面，默认状态下为最早点入的页面
    def get_max(self, b):
        max = -1
        flag = 0
        for i in range(0, self.M):
            if b[i].time > max:
                max = b[i].time
                flag = i
        return flag

    # 判断页面是否已在内存中（fold为需要判断的页面）
    def equation(self, fold, b):
        for i in range(0, self.M):
            if fold == b[i].num:
                return i  # 返回页面序号
        return -1

    # LRU 算法
    def lru(self, fold):
        val = self.equation(fold, self.b)
        if val >= 0:
            self.b[val].time = 0  # 如果已经存在则刷该页面新时间
            for i in range(0, self.M):
                if i != val:  # 其余页面时间加一
                    self.b[i].time += 1
        else:
            self.queue.append(fold)
            self.k += 1  # 新页调入就得加一
            val = self.get_max(self.b)  # 找到最旧的页面
            self.b[val].num = fold  # 替换该页面
            self.b[val].time = 0
            for i in range(0, self.M):
                if (i != val):  # 其余页面时间加一
                    self.b[i].time += 1

    # OPT 算法
    def opt(self, fold, index):
        # index记录当前页序号
        max = -1
        val = self.equation(fold, self.b)
        if val >= 0:
            pass
        else:
            self.queue.append(fold)
            self.k += 1

            for i in range(0, self.M):
                for j in range(index + 1, self.N):
                    if self.b[i].num == self.a[j]:
                        # 这里的时间指的是距离下次使用的时间
                        self.b[i].time = j - i
                        break
                    else:  # 不会再用到的设置非常大的时间
                        self.b[i].time = 999

            for i in range(0, self.M):
                if self.b[i].num == -1:  # 如果有空位
                    val = i
                    break;
                else:
                    if self.b[i].time > max:  # 找到缓冲区时间最长的
                        max = self.b[i].time
                        val = i
            self.b[val].num = fold

    def reset(self):  # 重置内存区、队列等，便于更换算法
        self.b = [page(-1, self.M - i - 1) for i in range(0, self.M)]
        self.c = [[-1 for i in range(0, self.N)] for j in range(0, self.M)]
        self.queue = []
        self.k = -1

    # 打印内存状态
    def Myprint(self):
        self.print_string()
        for i in range(0, self.N):  # 打印第一行 即要求存入的页面序列
            print("|%2d" % (self.a[i]), end=" ")  # 两位整数，空格结尾
        print("|")

        self.print_string()
        for i in range(0, self.M):
            for j in range(0, self.N):
                if self.c[i][j] == -1:
                    print("|%2c" % (32), end=" ")  # 无页面打印空格
                else:
                    print("|%2d" % (self.c[i][j]), end=" ")
            print("|")

        self.print_string()
        print("调入队列为")
        for i in range(0, self.k + 1):
            print("%2d" % (self.queue[i]), end=" ")
        print("\n缺页次数为：%6d\n缺页率：%16.6f" % (self.k + 1, (float)(self.k + 1) / self.N))

    # 主程序
    def process(self):
        # lru算法
        self.reset()
        for i in range(0, self.N):
            self.lru(self.a[i])
            # 记录当前的内存单元中的页面
            for j in range(0, self.M):
                self.c[j][i] = self.b[j].num
        print("lru算法内存状态为：")
        self.Myprint()

        # opt 算法
        self.reset()
        for i in range(0, self.N):
            self.opt(self.a[i], i)
            # 记录当前的内存单元中的页面
            for j in range(0, self.M):
                self.c[j][i] = self.b[j].num
        print("opt算法内存状态为：")
        self.Myprint()


if __name__ == "__main__":
    a = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    N = len(a)
    M = 4  # 可以改为3或其他大小
    main(M, N, a)
