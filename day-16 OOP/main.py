from turtle import Turtle, Screen


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# pokemon = ["Pikachu", "Charizard", "Ash", "Tüzesgyík"]
# type = ["Áramos", "Vizes", "Buzi", "Tüzes"]
# table.add_column("Pokemon", pokemon)
# table.add_column("Type", type)
# table.align = "c"
# print(table)


