import turtle
import random
from turtle import Turtle, Screen
turtle.colormode(255)

my_screen = Screen()
tim = Turtle()

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim.penup()
tim.speed("fastest")
tim.hideturtle()

for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        tim.setpos(x, y)
        tim.dot(20, random.choice(color_list))

my_screen.exitonclick()
