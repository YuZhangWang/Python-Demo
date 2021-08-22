import turtle as t
import random as rd


# 颜色随机函数
def rgb():
    r = rd.uniform(0, 1)
    g = rd.uniform(0, 1)
    b = rd.uniform(0, 1)
    t.pencolor(r, g, b)


# 彩色蟒蛇
def Colourful():
    t.setup(650, 350, 200, 200)
    t.penup()
    t.fd(-250)
    t.pendown()
    t.pensize(25)
    rgb()
    t.seth(-40)
    for i in range(4):
        rgb()
        t.circle(40, 80)
        rgb()
        t.circle(-40, 80)
        rgb()
    rgb()
    t.circle(40, 80 / 2)
    rgb()
    t.fd(40)
    rgb()
    t.circle(16, 180)
    rgb()
    t.fd(40 * 2 / 3)
    t.done()


Colourful()
