def Judge():
    n = 0
    for i in range(1000, 3001):
        if (i % 2 == 0):
            n += 1
            if (n % 33 != 0 and i != 3000):
                print("%6d" % i, end='')
            else:
                print("%6d" % i)


Judge()
