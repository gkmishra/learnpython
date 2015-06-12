import turtle

def draw_square(some_turtle):
    counter = 0
    while counter < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        counter = counter + 1

window = turtle.Screen()
window.bgcolor("red")
john = turtle.Turtle()
john.shape("arrow")
john.color("green")
john.speed("2")
for i in range(1,37):
    draw_square(john)
    john.right(10)
window.exitonclick()
