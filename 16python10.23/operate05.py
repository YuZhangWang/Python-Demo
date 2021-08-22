# P93 3.4
def Palindrome():
    a = input('请输入任意一位自然数:')
    b = a[::-1]
    if a == b:
        print('{}是回文数'.format(a))
    else:
        print('{}不是回文数'.format(a))


Palindrome()
