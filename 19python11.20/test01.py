# P151 5.1
def TianZige(h, l):
    # d是两个空格
    a, b, c, d = "+", "--", "|", "  "
    hang = 7 * b + a
    ch = 7 * d + c
    for i in range(h):
        print(a + hang * l)
        print(c + ch * l)
        print(c + ch * l)
        print(c + ch * l)
        print(c + ch * l)
    print(a + hang * l)


h, l = eval(input("请输入行和列(用逗号隔开):"))
TianZige(h, l)
