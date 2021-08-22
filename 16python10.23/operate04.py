# P93 3.2
def DayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0, 1, 2]:
            dayup = dayup * 1
        else:
            dayup = dayup * (1 + df)
    print("连续学习365天后能力值为:{:.2f}".format(dayup))


dayfactor = 0.01
DayUp(dayfactor)
