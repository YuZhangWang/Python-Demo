import turtle as t


def Hexagons():
    t.setup(650, 350, 200, 200)
    t.seth(30)
    for i in range(6):
        t.fd(30)
        t.left(120)
        t.fd(30)
        t.left(120)
        t.fd(30)
        t.left(120)

        t.fd(30)
        t.right(60)
    t.done()


Hexagons()
