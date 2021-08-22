# (2)百钱买百鸡
def HundredDollarsForChickens():
    cock = 1
    hen = 1
    chick = 1
    flag = 0
    for cock in range(21):
        for hen in range(34):
            for chick in range(101):
                if (cock * 5 + hen * 3 + chick == 100):
                    print("公鸡有{}只，母鸡有{}只，小鸡有{}只".format(cock, hen, chick))
                    flag = 1
                    break


HundredDollarsForChickens()
