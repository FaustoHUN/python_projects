import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
my_screen = Screen()

# tim.shape("turtle")
tim.color("blue")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


# Négyzetet rajzol
def draw_square():
    for t in range(4):
        tim.forward(100)
        tim.left(90)


# Szagattot vonalat rajzol
def underline():
    for i in range(50):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()


# Alakzatokat rajzol
def draw_forms():
    for i in range(3, 11):
        angel = 360 / i
        tim_color = random_color()
        tim.pencolor(tim_color)
        for t in range(i):
            tim.forward(100)
            tim.left(angel)


# Random forog és mozog
def random_move():
    tim.width(10)
    tim.speed(0)

    angels = [0, 90, 180, 270, 360]

    for i in range(100):
        tim.color(random_color())
        tim.setheading(random.choice(angels))
        tim.forward(25)


# Gyökvonás jel
def gyokvonas_jel():
    tim.pensize(15)
    tim.forward(10)
    tim.right(60)
    tim.forward(40)
    tim.left(120)
    tim.forward(100)
    tim.right(60)
    tim.forward(100)


def draw_spirograph(size_of_gap):
    tim.speed(0)
    rounds=int(360/size_of_gap)
    for _ in range(rounds):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size_of_gap)


draw_spirograph(1)
my_screen.exitonclick()
