import turtle


def square(size):
    if size <= 1:
        return None
    for _ in range(4):
        turtle.fd(size)
        turtle.right(90)
    turtle.right(10)
    turtle.up()
    turtle.fd(size*0.05)
    turtle.pd()
    square(size - 10)


def main():
    turtle.up()
    turtle.goto(0, 0)
    turtle.pd()
    a = int(input('Длина стороны:'))
    square(a)
    turtle.done()


main()
