import turtle

turtle.speed(200)
def fraktal(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        fraktal(order-1, size)
        turtle.left(90)
        fraktal(order-1, 2*size/3)
        turtle.right(180)
        fraktal(order-1, 2*size/3)
        turtle.left(90)
        fraktal(order-1, size)


def main():
    turtle.up()
    turtle.goto(-100, -200)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    fraktal(n, a)
    turtle.done()


main()
