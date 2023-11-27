import turtle

def levy(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        turtle.left(45)
        levy(order-1, size/2)
        turtle.right(90)
        levy(order-1, size/2)
        turtle.left(45)

def main():
    turtle.up()
    turtle.goto(-100, 0)
    turtle.pd()
    turtle.speed(100)
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    levy(n, a)
    turtle.done()


main()
