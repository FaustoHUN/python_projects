from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
tim.shape("turtle")
tim.color("green")
tim.pensize(5)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_canvas():
    my_screen.resetscreen()
    tim.color("green")
    tim.pensize(5)


def no_draw():
    tim.penup()


def draw():
    tim.pendown()


my_screen.listen()
my_screen.onkey(key="c", fun=clear_canvas)
my_screen.onkey(key="Up", fun=move_forward)
my_screen.onkey(key="Down", fun=move_backward)
my_screen.onkey(key="Left", fun=turn_left)
my_screen.onkey(key="Right", fun=turn_right)
my_screen.onkey(key="n", fun=no_draw)
my_screen.onkey(key="m", fun=draw)

my_screen.exitonclick()
