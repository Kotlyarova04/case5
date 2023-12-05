import turtle

turtle.speed(200)
def fraktal(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        fraktal(order - 1, size)
        turtle.left(60)
        fraktal(order - 1, 2 * size / 3)
        turtle.right(120)
        fraktal(order - 1, 2 * size / 3)
        turtle.left(60)
        fraktal(order - 1, size/2)
        turtle.left(60)
        fraktal(order-1, 2*size/3)
        turtle.right(120)
        fraktal(order - 1, 2*size/3)
        turtle.left(60)
        fraktal(order - 1, size)

def main():
    turtle.up()
    turtle.goto(-300, 0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    for _ in range(2):
        fraktal(n, a)
        turtle.right(180)
    turtle.done()

main()
