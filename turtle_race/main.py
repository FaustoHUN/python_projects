import turtle
from turtle import Turtle, Screen
import random

my_screen = Screen()

my_screen.setup(500, 400)

user_bet = my_screen.textinput(title="Make a bet!", prompt="Which turtle will win the game? Choose a color: ").lower()

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
y = -120

is_race_on = False

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

if winning_color == user_bet:
    print(f"Well done! The winner is {winning_color}!")
else:
    print(f"I'm sorry, you lose! The winner is {winning_color}.")

my_screen.exitonclick()
