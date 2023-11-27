import turtle


def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order - 1, size / 4)
        turtle.left(90)
        koch(order - 1, size / 4)
        turtle.right(90)
        koch(order - 1, size / 4)
        turtle.right(90)
        koch(order - 1, size / 2)
        turtle.left(90)
        koch(order - 1, size / 4)
        turtle.left(90)
        koch(order - 1, size / 4)
        turtle.right(90)
        koch(order - 1, size / 4)


def main():
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)
    turtle.done()


main()
