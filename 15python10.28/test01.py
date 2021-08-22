# 10.28上课笔记
print(pow(2, 2))
print(2 ** 2)
print(4 ** 0.5)
print(1010)  # 十进制
print(0B1111110010)  # 二进制
print(0O1762)  # 八进制
print(0X3f2)  # 十六进制

'''round(x, d)：对x四舍五入，d是小数截取位数'''
print(round(0.1 + 0.2) == 0.3)
print(round(0.1 + 0.2, 1) == 0.3)

# 数值运算符
print(100 / 3)  # 实数除法
print(100 // 3)  # 整数除法
print(round(100 / 3, 0))

# 二元操作符号
x = 2
x **= 2
print(x)

# 运算函数
print(abs(-10))
print(divmod(10, 3))  # 同时输出商和余数,(x//y,x%y)
print(pow(10, 3, 2))  # (x**y)%z
print(max(1, 10, 100, 1000))
print(min(1, 10, 100, 1000))
print(int(123.45))  # 整数
print(float(123))  # 浮点数
print(complex(123))  # 复数

x = (2 ** 4 + 7 - 3 * 4) / 5
print(x)
y = ((1 + 3 ** 2) * (16 % 7)) / 7
print(y)

'''
运算符优先级
**
+ - 取正负
* / % //
+ - 加减
'''

x = 1
x *= 3 + 5 ** 2  # x=x*(3 + 5 ** 2)
print(x)

x = 32 - 3 ** 2 + 8 // 3 ** 2 * 10
print(x)

x = 3 * 4 ** 2 / 8 % 5
print(x)

x = 365
dayup = pow(1.01, x)
daydown = pow(0.99, x)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))


def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup = dayup * (1 - df)
        else:
            dayup = dayup * (1 + df)
    return dayup


dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))
