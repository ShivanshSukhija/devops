import turtle
 
# Creating a turtle object(pen)
pen = turtle.Turtle()
 
# Defining method to draw a colored circle
# with a dynamic radius
def ring(col, rad):
 
    # Set the fill
    pen.fillcolor(col)
 
    # Start filling the color
    pen.begin_fill()
 
    # Draw a circle
    pen.circle(rad)
 
    # Ending the filling of the color
    pen.end_fill()
 
##########################Main Section#############################
import turtle

turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('red','pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()