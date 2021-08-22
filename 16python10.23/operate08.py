def License():
    for i in range(32, 99):
        a = pow(i, 2)
        b = a // 1000
        c = (a - b * 1000) // 100
        d = (a - b * 1000 - c * 100) // 10
        e = a - b * 1000 - c * 100 - d * 10
        if (b == c and d == e and b != d):
            print("该卡车车牌号为:{}".format(a))


License()
