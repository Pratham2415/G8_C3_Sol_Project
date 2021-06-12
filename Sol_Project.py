import turtle

length = 10

while length <= 150:
    for i in range(10):
        turtle.pencolor("red")
        turtle.forward(length)
        turtle.right(89)
        length += 0.5
        break
    turtle.pencolor("green")
    turtle.forward(length)
    turtle.right(89)
    length += 0.5