import turtle

eye = turtle.Turtle()

eye.screen.bgcolor("black")
eye.color("white")

eye.speed(70)

for i in range(180):
    eye.forward(100)
    eye.right(30)
    eye.forward(20)
    eye.left(60)
    eye.forward(50)
    eye.right(30)
    eye.penup()
    eye.setposition(0, 0)
    eye.pendown()
    eye.right(2)

turtle.done()
