import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed("fast")
    iterations = 4
    counter = 0
    while counter < 4 :
        brad.forward(100)
        brad.right(90)
        counter = counter + 1
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    troy = turtle.Turtle()
    troy.shape("triangle")
    troy.color("yellow")
    iterations = 3
    counter = 0
    while counter < 3 :
        troy.forward(200)
        troy.right(120)
        counter = counter + 1
    window.exitonclick()

draw_shapes()
