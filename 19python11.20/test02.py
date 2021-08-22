# P151 5.4
def mymulti(*b):
    a = 1
    for i in b:
        a *= i
    return a


print(mymulti(1, 2, 3, 4, 5))
