from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(height=500, width=500)
colors = ['red', 'blue', 'green', 'orange', 'black', 'yellow']
user_bet = screen.textinput(f"Place your bet", f"Which Turtle will win the race? {colors}: ")
print(user_bet)

print(colors)
y_position = [-75, -45, -15, 15, 45, 75]
turtle_list = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[i])
    turtle_list.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_game_on = False
            if turtle.pencolor() == user_bet:
                print(f"You have Won! {turtle.pencolor()} won.")
            else:
                print(f"You have Lost! {turtle.pencolor()} won.")


screen.exitonclick()
