'''
创建一个大字典，大字典的键为数字，作为最后的输出顺序。而键所对应的值是字典类型的。用于储存作业的各个数据。
首先数据的初始化都默认是第一个作业被执行所生成的数据（方便找到第一个作业后可以直接跳过修改阶段）。
当作业名为Z时，作业的创建结束。
'''


# 创建进程
def Creat():
    dic = {}
    i = 0
    while True:
        name = input("请输入进程名(输入Z结束)：")
        if name == 'Z':
            return dic
        enter_time = eval(input("请输入进入时间："))
        run_time = eval(input("请输入运行时间："))
        values = {i: {'作业名': name,
                      '进入时间': enter_time,
                      '运行时间': run_time,
                      '开始时间': enter_time,
                      '完成时间': enter_time + run_time,
                      '周转时间': run_time,
                      '带权周转时间': 1}}
        dic.update(values)
        i += 1


'''
以进入时间为对象，使用冒泡排序对作业进行排序。索引越小对应的键里的进入时间越早，即作业被创建的越早，索引值越小。
'''


# 第一次排序
def first_sort(data):
    for i in range(len(data)):
        Min = data[i]
        cnt = i
        for j in range(i, len(data)):
            if Min['进入时间'] > data[j]['进入时间']:
                Min = data[j]
                cnt = j
        temp = data[i]
        data[i] = Min
        data[cnt] = temp


'''
少了这步就可能出现BUG(即还没创建就开始执行)。所以这一步就是在进行筛选，找出符合条件的作业。
'''


# 找出在作业结束前被创建的作业
def Select_enter_time(data, finish, i):
    dic = {}
    for j in range(i, len(data)):
        if finish >= data[j]['进入时间']:
            ans = {j: data[j]}
            dic.update(ans)
    return dic


'''
在符合条件的作业下，找出响应比最大的作业的索引，因为在主函数中需要进行小字典（即作业）的交换。
'''


# 找出响应比最大的作业相对应的索引
def Response(Filter, finish, i):
    MAX = (finish - Filter[i]['进入时间'] + Filter[i]['运行时间']) / Filter[i]['运行时间']
    MAX_cnt = i
    for j in range(i, len(Filter)):
        wait = finish - Filter[j]['进入时间']
        res_time = (wait + Filter[j]['运行时间']) / Filter[j]['运行时间']
        if MAX < res_time:
            MAX = res_time
            MAX_cnt = j
    return MAX_cnt


'''
修改开始时间、完成时间、周转时间、带权周转时间。
'''


# 修改数据
def Write(data, finish, i):
    data[i]['开始时间'] = finish
    data[i]['完成时间'] = finish + data[i]['运行时间']
    data[i]['周转时间'] = data[i]['完成时间'] - data[i]['进入时间']
    data[i]['带权周转时间'] = data[i]['周转时间'] / data[i]['运行时间']


'''
打印输出数据
'''


# 打印输出
def PPrint(data):
    SZ, SD = 0, 0
    for i in range(len(data)):
        print(data[i])
        SZ += data[i]['周转时间']
        SD += data[i]['带权周转时间']
    print("平均周转时间{0:.2f},平均带权周转时间{1:.2f}".format(SZ / len(data), SD / len(data)))


def main():
    data = Creat()
    first_sort(data)
    finish = data[0]['完成时间']
    for i in range(1, len(data)):
        Filter = Select_enter_time(data, finish, i)
        if Filter == {}:
            break
        Index = Response(Filter, finish, i)
        temp = data[i]
        data[i] = Filter[Index]
        Filter[Index] = temp
        Write(data, finish, i)
        finish = data[i]['完成时间']
    PPrint(data)


if __name__ == '__main__':
    main()
