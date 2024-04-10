import turtle
from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

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
my_food = Food()
my_board = Scoreboard()

my_screen.listen()
my_screen.onkey(fun=my_snake.up, key="Up")
my_screen.onkey(fun=my_snake.down, key="Down")
my_screen.onkey(fun=my_snake.left, key="Left")
my_screen.onkey(fun=my_snake.right, key="Right")

while game_is_on:
    my_screen.update()
    time.sleep(0.1)  # slows down the turtle
    my_snake.snake_move()

    # Detect collision with the food
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_board.increase_score()

    # Detect collision with the wall
    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        game_is_on = False
        my_board.game_over()

    # Detect collision with the wall
    # if head collides with any segment in the tail
    # game ends

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            my_board.game_over()

my_screen.exitonclick()
