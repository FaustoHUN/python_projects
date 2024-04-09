import turtle
from turtle import Screen
import time
from snake import Snake

# SCREEN SETUP SECTION

# Screen color enabled
turtle.colormode(255)
colors = [(155, 203, 7), (172, 219, 9)]  # 3310 RGB colors in a list
my_screen = Screen()
my_screen.setup(width=600, height=600)  # Size if the screen 600x600
my_screen.bgcolor(colors[1])  # 3310 snake-green color for the background
my_screen.title("My Snake Game")  # Title of the screen
my_screen.tracer(0)  # Don't refresh the screen until the update method

my_screen.update()
game_is_on = True

my_snake = Snake()

while game_is_on:
    my_snake.snake_move()
    my_screen.listen()
    my_screen.onkey(fun=my_snake.up, key="Up")
    my_screen.onkey(fun=my_snake.down, key="Down")
    my_screen.onkey(fun=my_snake.left, key="Left")
    my_screen.onkey(fun=my_snake.right, key="Right")
    my_screen.update()
    time.sleep(0.1)

my_screen.exitonclick()
# end test 2.0
