from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

my_screen = Screen()

my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("PONG!")
my_screen.tracer(0)

r_paddle = Paddle()
r_paddle.create_paddle(x=350, y=0)
ball = Ball()

l_paddle = Paddle()
l_paddle.create_paddle(x=-350, y=0)

my_screen.listen()
my_screen.onkey(fun=r_paddle.go_up, key="Up")
my_screen.onkey(fun=r_paddle.go_down, key="Down")

my_screen.onkey(fun=l_paddle.go_up, key="w")
my_screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    print(ball.move_speed)
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()

    # detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.ball_bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.ball_bounce_x()

    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()

my_screen.exitonclick()
