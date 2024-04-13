from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    def create_paddle(self, x, y):
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(x=x, y=y)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(y=new_y, x=self.xcor())

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(y=new_y, x=self.xcor())
