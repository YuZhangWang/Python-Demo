# P121 4.2
def CountDifferentCharacters():
    s = input("请输入一行字符:\n")
    English, number, space, other = 0, 0, 0, 0
    for i in s:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            English += 1
        elif i in '0123456789':
            number += 1
        elif i == ' ':
            space += 1
        else:
            other += 1
    print('英文字符数为{},数字字符数为{},空格字符数为{},其他字符数为{}'.format(English, number, space, other))

CountDifferentCharacters()
