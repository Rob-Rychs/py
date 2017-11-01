# Make sure you install tkinter by : **sudo apt-get install python-tk**

import turtle

def make_square(turtle):
	for i in range (1,5):
		turtle.forward(100)
		turtle.right(90)

def make_shape():
	window = turtle.Screen()
	window.bgcolor("green")
	kate = turtle.Turtle()
	kate.shape("turtle")
	kate.color("white")
	kate.speed(3)
	for i in range (1,37):
		make_square(kate)
		kate.right(10)

	window.exitonclick()

make_shape()
