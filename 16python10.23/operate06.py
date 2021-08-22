def Judge():
    n = 0
    for i in range(2000, 3201):
        if (i % 7 == 0 and i % 5 != 0):
            n += 1
            if (n % 6 != 0):
                print("%6d" % i, end='')
            else:
                print("%6d" % i)


Judge()
