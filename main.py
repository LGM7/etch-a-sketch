from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.speed('fastest')

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counterclockwise():
    tim.left(10)

def reset():
    tim.clear()
    tim.reset()

def random_color():
    color = ['green', 'red', 'blue', 'cyan', 'magenta']
    tim.color(random.choice(color))

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=reset)
screen.onkey(key="r", fun=random_color)

screen.exitonclick()