# P180 6.2
def Test(ls):
    tem = set(ls)
    if len(tem) == len(ls):
        print('False')
    else:
        print('True')


def getTest():
    lis = []
    ch = input("请输入判定元素，回车表示结束:")
    while ch != '':
        lis.append(ch)
        ch = input("请输入判定元素，回车表示结束:")
    Test(lis)


getTest()
