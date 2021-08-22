# FIFO.py
framePageNum = input("请输入分配给该作业的物理页框块数：")  # 物理页框块数
pageFrame = [None] * int(framePageNum)  # 物理页框
inputPages = input("请输入该作业的页面走向：")
pages = inputPages.split(" ")  # 页面走向
pageFrontNum = len(pages)  # 页面走向总次数
pageDesert = []  # 淘汰页面
pageMissNum = 0  # 缺页次数

count = 0;
helpNum = 0;
while (count < pageFrontNum):
    print("第" + str(count + 1) + "次：" + pages[count])

    isMiss = True  # 是否缺页
    isEmpty = True  # 是否有空位
    isExist = False  # 物理页框中是否存在本次页面走向

    # 判断物理页框中是否存在本次页面走向
    for page in pageFrame:
        if (pages[count] == page):
            isExist = True
    if (isExist == True):
        print("本次页面走向，页框中已经存在！")
        print("目前物理页框中页面走向为：", end="")
        for i in pageFrame:
            print(i, end=" ")
        print()
        print()
        count = count + 1
        continue

    # 判断物理页框中有无空位
    for page in pageFrame:
        if (page == None):
            isEmpty = True
            break
        else:
            isEmpty = False
    # 本次页面走向，物理页框中不存在，且有空位
    if (isExist == False and isEmpty == True):
        for n in range(len(pageFrame)):
            if (pageFrame[n] == None):
                pageFrame[n] = pages[count]
                break

    # 实现 FIFO 算法
    # 本次页面走向，物理页框中不存在，且没有空位
    if (isExist == False and isEmpty == False):
        pageDesert.append(pageFrame[helpNum % int(framePageNum)])
        print("本次淘汰页面：" + pages[count])
        pageFrame[helpNum % int(framePageNum)] = pages[count]
        helpNum = helpNum + 1

    # 计算缺页次数
    if (isMiss == True):
        pageMissNum = pageMissNum + 1

    print("目前物理页框中页面走向为：", end="")
    for i in pageFrame:
        print(i, end=" ")
    print()
    print()
    count = count + 1

print("缺页次数：" + str(pageMissNum) + "次")
print("一共调用：" + str(pageFrontNum) + "次")
print("缺页中断率：" + str(pageMissNum / pageFrontNum * 100) + "%")
print("淘汰页面：", end="")
for i in pageDesert:
    print(i, end=" ")
