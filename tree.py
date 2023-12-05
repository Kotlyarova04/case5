import turtle


def color_tree(n, size):
    if n == 0:
        return None
    else:
        turtle.forward(size)
        turtle.right(30)
        color_tree(n - 1, size*0.6)
        turtle.left(60)
        color_tree(n - 1, size*0.6)
        turtle.right(30)
        turtle.backward(size)


def main():
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    turtle.left(90)
    color_tree(n, a)
    turtle.done()


main()

