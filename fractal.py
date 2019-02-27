import turtle

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()

def line(size ,order):
    if order == 0:
        turtle.forward(size)
        return
    size //= 3
    line(size, order-1)
    turtle.left(60)
    line(size, order-1)
    turtle.right(120)
    line(size, order-1)
    turtle.left(60)
    line(size, order-1)


line(700, 4)
