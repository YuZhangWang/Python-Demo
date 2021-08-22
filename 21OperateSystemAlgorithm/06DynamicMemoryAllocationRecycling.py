import copy

'''
动态的一个适应算法就是每次都从头开始找
循环适应就是接着后面找
最优算法就是先把空闲的按由小到大排序然后再找
最坏算法就是按由大到小排序找
'''

p_sign = None
p_num = 0
time = 0


class node(object):
    def __init__(self, start, end, length, state=1, ID=0):
        self.start = start
        self.end = end
        self.length = length
        self.state = state  # state为1:内存未分配
        self.Id = ID  # ID为0是未分配，其余为任务编号


def showList(list):
    """展示空闲分区"""
    print("空闲分区如下")
    id = 1
    for i in range(0, len(list)):
        p = list[i]
        if p.state == 1:
            print(id, ' :start ', p.start, " end ", p.end, " length ", p.length)
            id += 1


def showList2(list):
    """展示已分配分区"""
    print("已分配分区如下")
    for i in range(0, len(list)):
        p = list[i]
        if p.state == 0:
            print(p.Id, ' :start ', p.start, " end ", p.end, " length ", p.length)


def free_k(taskID, li):
    for i in range(0, len(li)):
        p = li[i]
        if p.Id == taskID:
            p.state = 1
            x = i
            print("已释放", taskID, ' :start ', p.start, " end ", p.end, " length ", p.length)
            break

    # 向前合并空闲块
    if x - 1 > 0:
        if li[x - 1].state == 1:
            a = node(li[x - 1].start, li[x].end, li[x - 1].length + li[x].length, 1, 0)
            del li[x - 1]
            del li[x - 1]
            li.insert(x - 1, a)
            x = x - 1

    # 向后合并空闲块
    if x + 1 < len(li):
        if li[x + 1].state == 1:
            a = node(li[x].start, li[x + 1].end, li[x].length + li[x + 1].length, 1, 0)
            del li[x]
            del li[x]
            li.insert(x, a)
    showList(li)


# 首次适应算法
def alloc0(taskID, Tasklength, list):
    for i in range(0, len(list)):
        p = list[i]
        if p.state == 1 and p.length > Tasklength:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配", a.Id, ' :start ', a.start, " end ", a.end, " length ", a.length)
            del list[i]
            list.insert(i, node2)
            list.insert(i, a)
            # showList(list)
            return
        if p.state == 1 and p.length == Tasklength:
            print("已分配", taskID, ' :start ', p.start, " end ", p.end, " length ", p.length)
            p.state = 0
            showList(list)
            return
    print("内存空间不足")


# 循环首次适应算法
def alloc1(taskID, Tasklength, list):
    global p_sign, p_num, time
    if time == 0:
        p_sign = list[0]
        time = 1
    for i in range(0, len(list)):
        p = list[i]
        if (p.start - 1) == p_sign.end:
            p_num = i
    for i in range(p_num, len(list)):
        p = list[i]
        if p.state == 1 and p.length > Tasklength:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配", a.Id, ' :start ', a.start, " end ", a.end, " length ", a.length)
            p_sign = a
            del list[i]
            list.insert(i, node2)
            list.insert(i, a)
            # showList(list)
            return
        if p.state == 1 and p.length == Tasklength:
            print("已分配", taskID, ' :start ', p.start, " end ", p.end, " length ", p.length)
            p.state = 0
            showList(list)
            return
    for i in range(p_num):
        p = list[i]
        if p.state == 1 and p.length > Tasklength:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            p_sign = a
            del list[i]
            list.insert(i, node2)
            list.insert(i, a)
            showList(list)
            return
        if p.state == 1 and p.length == Tasklength:
            p.state = 0
            showList(list)
            return
    print("内存空间不足")


##最佳适应算法
def bubble_sort(list):
    # 冒泡排序
    count = len(list)
    for i in range(0, count):
        for j in range(i + 1, count):
            if list[i].length < list[j].length:
                list[i], list[j] = list[j], list[i]
    return list


def alloc2(taskID, Tasklength, li):
    q = copy.copy(li)
    q = bubble_sort(q)
    s = -1
    ss12 = -1
    for i in range(0, len(q)):
        p = q[i]
        if p.state == 1 and p.length > Tasklength:
            s = p.start
        elif p.state == 1 and p.length == Tasklength:
            ss12 = p.start
    if s == -1 and ss12 == -1:
        print("内存空间不足")
        return
    for i in range(0, len(li)):
        p = li[i]
        if p.start == s:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配", a.Id, ' :start ', a.start, " end ", a.end, " length ", a.length)
            del li[i]
            li.insert(i, node2)
            li.insert(i, a)
            # showList(li)
            return
        elif p.start == ss12:
            print("已分配", taskID, ' :start ', p.start, " end ", p.end, " length ", p.length)
            p.state = 0
            showList(li)
            return


##最坏适应算法
def bubble_sort2(list):
    # 冒泡排序
    count = len(list)
    for i in range(0, count):
        for j in range(i + 1, count):
            if list[i].length > list[j].length:
                list[i], list[j] = list[j], list[i]
    return list


def alloc3(taskID, Tasklength, li):
    q = copy.copy(li)
    q = bubble_sort2(q)
    s = -1
    ss12 = -1
    for i in range(0, len(q)):
        p = q[i]
        if p.state == 1 and p.length > Tasklength:
            s = p.start
        elif p.state == 1 and p.length == Tasklength:
            ss12 = p.start
    if s == -1 and ss12 == -1:
        print("内存空间不足")
        return
    for i in range(0, len(li)):
        p = li[i]
        if p.start == s:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配", a.Id, ' :start ', a.start, " end ", a.end, " length ", a.length)
            del li[i]
            li.insert(i, node2)
            li.insert(i, a)
            # showList(li)
            return
        elif p.start == ss12:
            print("已分配", taskID, ' :start ', p.start, " end ", p.end, " length ", p.length)
            p.state = 0
            showList(li)
            return


if __name__ == "__main__":
    while True:
        try:
            x = int(input("请选择:0首次适应算法，1循环首次适应算法，2最佳适应算法，3最坏适应算法,4退出程序"))
            # 从0位置开始，639位置结束，长度为640
            a = node(0, 639, 640, state=1, ID=0)
            b = []
            b.append(a)
            if x == 0:
                auto_num1 = int(input("请选择运行示例（0）还是手动分配内存（1）"))
                if auto_num1 == 0:
                    alloc0(1, 130, b)
                    alloc0(2, 60, b)
                    alloc0(3, 100, b)
                    showList2(b)
                    free_k(2, b)
                    alloc0(4, 200, b)
                    showList2(b)
                    free_k(3, b)
                    free_k(1, b)
                    showList2(b)
                    alloc0(5, 140, b)
                    alloc0(6, 60, b)
                    alloc0(7, 50, b)
                    free_k(6, b)
                    showList2(b)
                while True and auto_num1:
                    print("")
                    sele_0 = int(input("请选择:1、分配内存 2、释放分区 3、展示空闲分区表 4、展示已分配分区表 5、退出程序"))
                    if sele_0 == 1:
                        db_id = int(input("请输入要分配任务的ID"))
                        id_size = int(input("请输入要该任务需要的内存大小"))
                        alloc0(db_id, id_size, b)
                    elif sele_0 == 2:
                        fr_id = int(input("请输入要释放任务的ID"))
                        free_k(fr_id, b)
                    elif sele_0 == 3:
                        showList(b)
                    elif sele_0 == 4:
                        showList2(b)
                    elif sele_0 == 5:
                        break
                    else:
                        print("请重新输入")
            elif x == 1:
                auto_num1 = int(input("请选择运行示例（0）还是手动分配内存（1）"))
                if auto_num1 == 0:
                    alloc1(1, 130, b)
                    alloc1(2, 60, b)
                    alloc1(3, 100, b)
                    free_k(2, b)
                    alloc1(4, 200, b)
                    free_k(3, b)
                    free_k(1, b)
                    alloc1(5, 140, b)
                    alloc1(6, 60, b)
                    alloc1(7, 50, b)
                    free_k(6, b)
                    showList2(b)
                while True and auto_num1:
                    print("")
                    sele_0 = int(input("请选择:1、分配内存 2、释放分区 3、展示空闲分区表 4、展示已分配分区表 5、退出程序"))
                    if sele_0 == 1:
                        db_id = int(input("请输入要分配任务的ID"))
                        id_size = int(input("请输入要该任务需要的内存大小"))
                        alloc1(db_id, id_size, b)
                    elif sele_0 == 2:
                        fr_id = int(input("请输入要释放任务的ID"))
                        free_k(fr_id, b)
                    elif sele_0 == 3:
                        showList(b)
                    elif sele_0 == 4:
                        showList2(b)
                    elif sele_0 == 5:
                        break
                    else:
                        print("请重新输入")
            elif x == 2:
                auto_num1 = int(input("请选择运行示例（0）还是手动分配内存（1）"))
                if auto_num1 == 0:
                    alloc2(1, 130, b)
                    alloc2(2, 60, b)
                    alloc2(3, 100, b)
                    free_k(2, b)
                    alloc2(4, 200, b)
                    free_k(3, b)
                    free_k(1, b)
                    alloc2(5, 140, b)
                    alloc2(6, 60, b)
                    alloc2(7, 50, b)
                    free_k(6, b)
                    showList2(b)
                while True and auto_num1:
                    print("")
                    sele_0 = int(input("请选择:1、分配内存 2、释放分区 3、展示空闲分区表 4、展示已分配分区表 5、退出程序"))
                    if sele_0 == 1:
                        db_id = int(input("请输入要分配任务的ID"))
                        id_size = int(input("请输入要该任务需要的内存大小"))
                        alloc2(db_id, id_size, b)
                    elif sele_0 == 2:
                        fr_id = int(input("请输入要释放任务的ID"))
                        free_k(fr_id, b)
                    elif sele_0 == 3:
                        showList(b)
                    elif sele_0 == 4:
                        showList2(b)
                    elif sele_0 == 5:
                        break
                    else:
                        print("请重新输入")
            elif x == 3:
                auto_num1 = int(input("请选择运行示例（0）还是手动分配内存（1）"))
                if auto_num1 == 0:
                    alloc3(1, 130, b)
                    alloc3(2, 60, b)
                    alloc3(3, 100, b)
                    free_k(2, b)

                    alloc3(4, 200, b)
                    free_k(3, b)
                    free_k(1, b)
                    alloc3(5, 140, b)
                    alloc3(6, 60, b)
                    alloc3(7, 50, b)
                    free_k(6, b)
                    showList2(b)
                while True and auto_num1:
                    print("")
                    sele_0 = int(input("请选择:1、分配内存 2、释放分区 3、展示空闲分区表 4、展示已分配分区表 5、退出程序"))
                    if sele_0 == 1:
                        db_id = int(input("请输入要分配任务的ID"))
                        id_size = int(input("请输入要该任务需要的内存大小"))
                        alloc3(db_id, id_size, b)
                    elif sele_0 == 2:
                        fr_id = int(input("请输入要释放任务的ID"))
                        free_k(fr_id, b)
                    elif sele_0 == 3:
                        showList(b)
                    elif sele_0 == 4:
                        showList2(b)
                    elif sele_0 == 5:
                        break
                    else:
                        print("请重新输入")
            elif x == 4:
                break
            else:
                print("请输入正确的选项")
                continue
        except:
            print("请输入正确的选项")
