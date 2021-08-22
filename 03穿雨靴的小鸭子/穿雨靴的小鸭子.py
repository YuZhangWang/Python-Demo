# 穿雨鞋的小鸭
from turtle import *

# 扁嘴
pensize(2)

pu()
goto(-100, 100)  # 上嘴最高顶点
seth(-50)
pd()
color('#6C3100', '#FADD77')
begin_fill()
fd(16)
vertex_right = pos()  # 嘴最右顶点
rt(50)
fd(12)
vertex_down = pos()  # 下嘴最低顶点
rt(80)
fd(30)
circle(-3, 200)
vertex_left = pos()  # 嘴最左顶点
goto(-100, 100)
end_fill()
goto(vertex_left)  # 回到最左顶点
circle(-3, -200)  # 扁嘴
goto(vertex_right)

# 身体
# 头颈背尾曲线
color('#B6A88E')
pu()
goto(-100, 100)
pd()

seth(80)
circle(-36, 160)
fd(25)
circle(115, 20)
circle(60, 55)
circle(-200, 20)
circle(110, 20)
color('#7D6A4C')
circle(40, 40)
color('#B6A88E')
seth(-100)
circle(-180, 30)
circle(-20, 50)

# 右鸭腿
circle(20, 70)
color('#736856')
circle(-12, 120)
leg_pos1 = pos()  # 定位左腿位置
fd(25)

# 前胸肚曲线
pu()
goto(vertex_down)
pd()
seth(-10)
color('#B9AD9D')
circle(-40, 50)
circle(-80, 48)
color('#736856')
circle(250, 5)
circle(50, 75)
color('#B9AD9D')
circle(220, 28)

# 左鸭腿
pu()
seth(175)
fd(40)
pd()
seth(-120)
fd(8)
circle(-10, 120)
leg_pos2 = pos()  # 定位右腿位置
fd(15)

# 眼睛
color('black')
# 左眼
pu()
goto(vertex_down - (1, -29))
pd()
dot(4, 'black')  # 相比circle()，不需要再额外填充颜色
# 右眼
pu()
goto(vertex_down + (23, 20))
pd()
dot(4, 'black')

# 翅膀
color('#BCB2A6')
pu()
goto(vertex_down - (-75, 130))
seth(130)
pd()
circle(-25, 130)
circle(-100, 30)
fd(85)
point = pos()
rt(137)
fd(52)
circle(-100, 58)

pu()
goto(point)
lt(30)
pd()
fd(60)

pu()
goto(point)
pd()
lt(10)
fd(70)


# 腿部
# 左腿
def leg(pos0):  # 鸭腿绘制函数
    pensize(8)
    color('#ECC578')
    pu()
    goto(pos0)
    seth(0)
    fd(7)
    seth(-90)
    fd(8.5)
    pd()
    fd(20)  # 腿长


leg(leg_pos1)
leg(leg_pos2)


# 小红靴——函数
def boot(pos0):
    pensize(2)
    color('#B4070B', '#FBA06B')
    pu()
    goto(pos0)  # 靴子右上顶点
    pd()
    begin_fill()
    seth(140)
    circle(25, 80)
    seth(-80)
    fd(35)  # fd(30)左侧线条

    circle(-2, 60)  # 靴低
    fd(20)
    circle(4, 180)
    seth(5)
    fd(30)
    circle(2, 60)

    goto(pos0)  # 右侧线条
    end_fill()


boot(leg_pos1 - (-20, 30))
boot(leg_pos2 - (-20, 30))

# 小雨滴
color('#77DDFF', '#D8E8E5')
fd_ls = [200, 140, 250, 240, 230, 220, 180, 250]
lt_ls = [30, 60, 60, 100, 125, 170, 200, 330]
for i in range(8):
    pu()
    home()
    lt(lt_ls[i])
    fd(fd_ls[i])

    pd()
    seth(-78)
    fd(15)
    begin_fill()
    circle(-3, 200)
    end_fill()
    fd(15)

# 文字
pu()
goto(vertex_left)
seth(180)
fd(150)
seth(-90)
fd(300)
color('black')
write('code by YuZhangWang', font=("Arial", 15, "normal"))

hideturtle()
done()
