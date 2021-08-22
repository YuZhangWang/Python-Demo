p = 1
print('第10天吃之前还剩1个桃子')
for i in range(9, 0, -1):
    p = (p + 1) * 2
    print('第%s天吃之前还剩%s个桃子' % (i, p))
print('所以第1天共摘了%s个桃子' % p)
