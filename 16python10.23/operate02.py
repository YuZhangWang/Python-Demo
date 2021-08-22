import turtle as t


# 画
def isdrawing():
    t.pendown()
    t.fd(40)


# 不画
def notdrawing():
    t.penup()
    t.fd(20)


def Quadrilateral():
    t.Screen().setup(600, 600, 0, 0)
    for i in range(1, 5):
        notdrawing()
        isdrawing()
        notdrawing()
        t.seth(i * 90)
    t.done()


Quadrilateral()
