import turtle

def draw_kc(some_turtle):
    counter = 0
    # Draw the K
    some_turtle.goto(0,100)
    some_turtle.setpos(0,50)
    some_turtle.goto(50,100)
    some_turtle.setpos(0,50)
    some_turtle.goto(50,0)
    # Draw the C
    some_turtle.color("red")
    some_turtle.setpos(80,0)
    some_turtle.color("green")
    some_turtle.goto(130,0)
    some_turtle.setpos(80,0)
    some_turtle.goto(80,100)
    some_turtle.goto(130,100)

window = turtle.Screen()
window.bgcolor("red")
john = turtle.Turtle()
john.shape("arrow")
john.color("green")
john.speed("slow")
#for i in range(1,5):
draw_kc(john)
#    john.right(10)
window.exitonclick()
